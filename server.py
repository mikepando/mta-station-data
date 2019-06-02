from flask import Flask, render_template, request
import datetime as dt
import pandas as pd
from stationList import stationList 


app = Flask(__name__)
app.config["DEBUG"] = True

def readMtaData(url, week):
    df=pd.read_csv(url,skiprows=2)
    df.set_index("REMOTE",inplace=True);
    df.rename(columns={" STATION":"STATION"},inplace=True)
    df.pop(df.columns[-1])
    df["SWIPE_SUM"]=df.sum(axis=1)
    df["DATE"]=week.strftime("%b_%d_%Y")    # %b=Month name, %d=Month day, %Y=full year
    return df

def stringMonth(month):
    if month==1:
        fullMonth="January"
    elif month==2:
        fullMonth="February"
    elif month==3:
        fullMonth="March"
    elif month==4:
        fullMonth="April"
    elif month==5:
        fullMonth="May"
    elif month==6:
        fullMonth="June"
    elif month==7:
        fullMonth="July"
    elif month==8:
        fullMonth="August"
    elif month==9:
        fullMonth="September"
    elif month==10:
        fullMonth="October"
    elif month==11:
        fullMonth="November"
    else:
        fullMonth="December"
    return fullMonth

def dayWeek(startDate):
    weekDay=startDate.weekday() 
    if (weekDay == 2 or weekDay == 3 or weekDay == 4):
        if weekDay == 2:
            time = 3
        elif weekDay == 3:
            time = 2
        else:
            time = 1
        days = dt.timedelta(days=time)
        startDate = startDate + days
    elif(weekDay == 6 or weekDay == 0 or weekDay == 1):
        if weekDay == 6:
            time = 1
        elif weekDay == 0:
            time = 2
        else:
            time = 3
        days = dt.timedelta(days=time)
        startDate = startDate - days
    return startDate

def url_Chart(fixedDate,station):
    weekOne=dt.timedelta(weeks=1)
    weekTwo=fixedDate+weekOne
    weekThree=weekTwo+weekOne
    weekFour=weekThree+weekOne
    
    url=fixedDate.strftime("http://web.mta.info/developers/data/nyct/fares/fares_%y%m%d.csv")
    df1=readMtaData(url,fixedDate)
    
    url=weekTwo.strftime("http://web.mta.info/developers/data/nyct/fares/fares_%y%m%d.csv")
    df2=readMtaData(url,weekTwo)
    
    url=weekThree.strftime("http://web.mta.info/developers/data/nyct/fares/fares_%y%m%d.csv")
    df3=readMtaData(url,weekThree)
    
    url=weekFour.strftime("http://web.mta.info/developers/data/nyct/fares/fares_%y%m%d.csv")
    df4=readMtaData(url,weekFour)

    st1=df1.loc[station]
    st2=df2.loc[station]
    st3=df3.loc[station]
    st4=df4.loc[station]
    allData=pd.DataFrame([st1,st2,st3,st4])
    
    allData.plot(kind="bar",x="DATE",y="SWIPE_SUM", title=station,
                 figsize=(14,12)).get_figure().savefig("static/station.png")
    allData.plot(kind="barh",x="DATE",y="SWIPE_SUM", title=station,
                 figsize=(14,12)).get_figure().savefig("static/station1.png")
    return st1
@app.route('/', methods=["GET","POST"])
def index():
    return render_template('main_page.html',data=stationList)

@app.route("/response", methods=["POST"])
def response():
    year=request.form["year"]
    month=request.form["month"]
    station=request.form["station"]
    startDate=dt.datetime(int(year), int(month), 1)
    
    fullMonth=stringMonth(int(month))
    fixedDate=dayWeek(startDate)
    st1=url_Chart(fixedDate,station)
    
    return render_template('response.html',station=st1["STATION"],month=fullMonth,
                            year=year)
    
if __name__ == '__main__':
    app.run(debug=True, port=5001)

