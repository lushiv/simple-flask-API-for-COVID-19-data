from flask import Flask,jsonify,request
import requests
from bs4 import BeautifulSoup 

app = Flask(__name__)


def get_coronavirus_country_data_scraper(cname):
    total_result = []
    country = cname
    url = "https://www.worldometers.info/coronavirus/country/{countryname}/".format(countryname=country)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result = soup.find_all('div', class_ = "maincounter-number")

        for i in result:
            total_result.append(i.find("span").text)


    else:
        total_result.append("No Result")

    return total_result



@app.route("/info/<country_name>", methods =["GET"])
def findinformation(country_name):
    country = country_name
    try:
        return jsonify({

            "Total Coronavirus Cases": get_coronavirus_country_data_scraper(country)[0], 
            "Total Deaths": get_coronavirus_country_data_scraper(country)[1],
            "Total Recovered": get_coronavirus_country_data_scraper(country)[2]
        }
        )
    

    except:
        return jsonify({"No Country Found":""})




if __name__ == "__main__":
    app.run()