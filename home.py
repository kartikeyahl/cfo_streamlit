import streamlit as st
import pandas as pd
#import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import threading
import plotly.express as px
from PIL import Image
st.set_page_config(layout="wide")
rad=st.sidebar.radio("Navigation",["Home","Electricty consumption","Air index","Temperature stats", "Ice coverage stats","CO2 stats (choose country from below)","Indian statewise electricity stats"])

if rad=="Home":
    image = Image.open("l.png")
    st.image(image, width = 500)
    st.title('Climatic Fluctuations Onlooker')
    st.markdown(""" 
It is a dashboard dedicated to the statistics and trends of major climat chage causes, which are:\n
**Electricity Consumption**\n
**Air Index**\n
**Temperature Change Stats**\n
**Ice Coverage Stats**\n
**CO2 Stats**\n
**Indian State-wise Electricity Stats**\n
\n\n
-------
-------
\n\n
Climate change is here and this is what it looks like: more frequent flooding in the central US, a longer and more costly wildfire season in California, and droughts across the Great Plains. Like investing in your retirement, the sooner we take action, the better chance we have at preventing the direst impacts of our rapidly warming world. The world’s best scientists tell us that to undo the most extreme scenarios of climate change, 2020 must be the year for coordinated, comprehensive climate action. But we’ve got a lot of work to do before then.

The good news is that global momentum around climate change is building toward a crescendo. Six in 10 Americans are now either “alarmed" or “concerned” about climate change, a number that has more than doubled in the past five years. Hundreds of thousands of people from all walks of life, including students, teachers, communities of faith, health care professionals are taking to the streets to demand climate action. And more than 500 global companies have committed to set climate goals based on the best available science.

Responding to this call to action, governments worked together to develop the Paris Climate Agreement in 2015—an unprecedented step to reduce worldwide emissions. Nearly 200 countries pledged to reduce emissions and keep temperature rise well below 2° C (3.6° F).
    """)

    with open("file.txt", "r") as f:
        a = f.readline()  # starts as a string
        a = 0 if a == "" else int(a)
    
    st.markdown('''
    \n
    ----
    ''')

    if st.button("I take a pledge to limit my carbon footprints"):
        a += 1  
        with open("file.txt", "w") as f:
            f.truncate()
            f.write(f"{a}")
            
    st.markdown('''#***Total pledges taken: {}***'''.format(a))
    st.balloons()



if rad=="Electricty consumption":
    st.title('ELECTRICITY CONSUMPTION')
    image = Image.open('d8.jpg')
    st.image(image, width = 900)
    st.markdown(""" 
    The estimated CO2 emission from the world's electrical power industry is 10 billion tonnes yearly. This results in an increase in the Earth's levels of atmospheric carbon dioxide, which enhances the greenhouse effect and contributes to global warming. \n
    Almost all forms of electricity generate waste. For example, natural gas releases carbon dioxide and nitrogen oxide. Earth's atmosphere traps these gases, leading to air pollution and smog. Weather patterns and geological variations can affect the prevalence of smog in a particular area.\n
    **Solution: **
    Going energy efficient is considered expensive but more efficient can be as simple as changing a lightbulb. In general, you should have a habit to switch off all computers, televisions, telephones, air conditioning units, lights, and other electronics when you're not using them.


    Analysis of electricty consumption on the basis of:\n
    * Hours
    * Days of week
    * Months
    * Quarter
    * Days of month
    * Weeks of Year
    """)
    '''\n'''

    sl1=st.selectbox("Select Plot",['ALL','Electricity in megawatts vs hours','Electricity in megawatts vs days of week','Electricity in megawatts vs month','Electricity in megawatts vs quarter','Electricity in megawatts vs days in month','Electricity in megawatts vs weeks of year'])
    
    @st.cache()
    def loadd():
        dom_hourly = pd.read_csv("DOM_hourly.csv")

        dom_hourly['Datetime'] = pd.to_datetime(dom_hourly['Datetime'])
        dom_hourly['hour'] = dom_hourly['Datetime'].dt.hour
        dom_hourly['dayofweek'] = dom_hourly['Datetime'].dt.dayofweek
        dom_hourly['quarter'] = dom_hourly['Datetime'].dt.quarter
        dom_hourly['month'] = dom_hourly['Datetime'].dt.month
        dom_hourly['dayofyear'] = dom_hourly['Datetime'].dt.dayofyear
        dom_hourly['day'] = dom_hourly['Datetime'].dt.day
        dom_hourly['weekofyear'] = dom_hourly['Datetime'].dt.weekofyear
        return dom_hourly
    dom_hourly=loadd()
    
    if sl1=="Electricity in megawatts vs hours" or sl1=="ALL":
        l1=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
        mean_hour = dom_hourly.groupby("hour")["DOM_MW"].mean()
        sns.barplot(x=l1, y=mean_hour, data=mean_hour)
        sns.set(rc={'figure.figsize':(8,8.27)})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.title('Electricity in megawatts vs hours',fontsize=20)
        plt.xlabel('Hours')
        plt.ylabel('Electricity in megawatts')
        st.pyplot()
        mean_hour
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

    if sl1=="Electricity in megawatts vs days of week" or sl1=="ALL" :
        l=['0','1','2','3','4','5','6']
        data1=dom_hourly.groupby("dayofweek")["DOM_MW"].mean()
        sns.barplot(x=l, y=data1, data=data1)
        sns.set(rc={'figure.figsize':(8,8.27)})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.title('Electricity in megawatts vs days of week',fontsize=20)
        plt.xlabel('days of week')
        plt.ylabel('Electricity in megawatts')
        st.pyplot()
        data1

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''
    if sl1=="Electricity in megawatts vs month" or sl1=="ALL":

        l2=['1','2','3','4','5','6','7','8','9','10','11','12']
        data2=dom_hourly.groupby("month")["DOM_MW"].mean()
        sns.barplot(x=l2, y=data2, data=data2)
        sns.set(rc={'figure.figsize':(8,8.27)})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.title('Electricity in megawatts vs month',fontsize=20)
        plt.xlabel('Months')
        plt.ylabel('Electricity in megawatts')
        st.pyplot()
        data2

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

    if sl1=="Electricity in megawatts vs quarter" or sl1=="ALL":

        l3=['1','2','3','4']
        data3= dom_hourly.groupby("quarter")["DOM_MW"].mean()
        sns.barplot(x=l3, y=data3, data=data3)
        sns.set(rc={'figure.figsize':(8,8.27)})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.title('Electricity in megawatts vs quarter',fontsize=20)
        plt.xlabel('Quarters')
        plt.ylabel('Electricity in megawatts')
        st.pyplot()
        data3

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''
    
    if sl1=="Electricity in megawatts vs days in month" or sl1=="ALL":

        l4=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
        data4= dom_hourly.groupby("day")["DOM_MW"].mean()
        sns.barplot(x=l4, y=data4, data=data4)
        sns.set(rc={'figure.figsize':(8,8.27)})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.title('Electricity in megawatts vs days in month',fontsize=20)
        plt.xlabel('Days')
        plt.ylabel('Electricity in megawatts')
        st.pyplot()
        data4

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

    if sl1=="Electricity in megawatts vs weeks of year" or sl1=="ALL":

        l5=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53']
        plt.figure(figsize=(14,8))
        data5= dom_hourly.groupby("weekofyear")["DOM_MW"].mean()
        sns.barplot(x=l5, y=data5, data=data5)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.title('Electricity in megawatts vs weeks of year',fontsize=30)
        plt.xlabel('weeks of year',fontsize=18)
        plt.ylabel('Electricity in megawatts',fontsize=18)
        st.pyplot()
        data5








if rad=="Air index":
    st.title('Air Index')   
    image = Image.open('download1.jpg')
    st.image(image, width = 800) 
    st.markdown('''
    Climate change can impact air quality and, conversely, air quality can impact climate change. Changes in climate can result in impacts to local air quality. Emissions of pollutants into the air can result in changes to the climate. Ozone in the atmosphere warms the climate, while different components of particulate matter (PM) can have either warming or cooling effects on the climate. For example, black carbon, a particulate pollutant from combustion, contributes to the warming of the Earth, while particulate sulfates cool the earth's atmosphere.



    **NO2:** Combustion from power sources or Transport.

    **SO2:** Coal burning, Oil burning, Manufacturing of Sulphuric acid.

    **rspm:** Respirable suspended particulate matter. A sub form of spm and are responsible for respiratory diseases.

    **spm:** Suspended particulate matter and are known to be the deadliest form of air pollution. They are microscopic in nature and are found to be suspended in earth's atmosphere.

    **pm2_5:** Suspended particulate matter with diameters less than 2.5 micrometres. They tend to remain suspended for longer durations and potentially very harmful.
    ''')
    sl2=st.selectbox("Select Plot",['ALL','SO2','NO2','RSPM','SPM','PM 2.5'])
    
    if sl2=="SO2" or sl2=="ALL":
        st.title("State vs SO2")
        image = Image.open('logo.jpg')
        st.image(image, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

    if sl2=="NO2" or sl2=="ALL":
        st.title("State vs NO2")
        imag = Image.open('logo2.jpg')
        st.image(imag, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''
    if sl2=="RSPM" or sl2=="ALL":
        st.title("State vs RSPM")
        ima = Image.open('logo3.jpg')
        st.image(ima, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

    if sl2=="SPM" or sl2=="ALL":  
        st.title("State vs SPM") 
        im = Image.open('logo4.jpg')
        st.image(im, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''
    if sl2=="PM 2.5" or sl2=="ALL":
        st.title("State vs PM 2.5")
        i = Image.open('logo5.jpg')
        st.image(i, width = 1000)





if rad=="Temperature stats":
    st.title("Temperature Stats")
    imago = Image.open('hightemp.jpg')
    st.image(imago, width = 400)
    st.markdown('''
    average temperatures at the Earth's surface are increasing and are expected to continue rising. Because climate change can shift the wind patterns and ocean currents that drive the world's climate system, some areas are warming more than others, and some have experienced cooling.\n
    If people keep adding greenhouse gases into the atmosphere at the current rate, the average temperature around the world could increase by about 4 to 12°F by the year 2100. If we make big changes, like using more renewable resources instead of fossil fuels, the increase will be less—about 2 to 5°F.
    ''')

    sl3=st.selectbox("Select Plot",['ALL','Land and ocean temperature','Change in land and ocean temperature','Avg. temperature on land by months','Avg. temperature seasonwise over the years','Countries with highest avg. temperature','Top 10 coolest states(India)','Top 10 hotest states(India)','Expected temperature changes in 2050'])
    
    if sl3=="Land and ocean temperature" or sl3=="ALL":
        image = Image.open('l1.jpg')
        st.image(image, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''
    if sl3=="Change in land and ocean temperature" or sl3=="ALL":
        imag = Image.open('l2.jpg')
        st.image(imag, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''
    if sl3=="Avg. temperature on land by months" or sl3=="ALL":
        ima = Image.open('l3.jpg')
        st.image(ima, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''
    
    if sl3=="Avg. temperature seasonwise over the years" or sl3=="ALL":
        im = Image.open('l4.jpg')
        st.image(im, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

    if sl3=="Countries with highest avg. temperature" or sl3=="ALL":
        i = Image.open('l5.jpg')
        st.image(i, width = 700)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''
    
    if sl3=="Top 10 coolest states(India)" or sl3=="ALL":
        ii = Image.open('l6.jpg')
        st.image(ii, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''
    
    if sl3=="Top 10 hotest states(India)" or sl3=="ALL":
        iii = Image.open('l7.jpg')
        st.image(iii, width = 1000)

    if sl3=="Expected temperature changes in 2050" or sl3=="ALL":
        iiio = Image.open('temp.jpg')
        st.image(iiio, width = 1000)








if rad=="Ice coverage stats":
    st.title("Ice coverage stats")
    image = Image.open('d11.jpg')
    st.image(image, width = 900)
    st.markdown('''
    With less ice present, the dark surface of ocean water absorbs considerably more sunlight energy, leading to further warming of the atmosphere and more melting of ice, which leads to further warming.\n
    We lose Arctic sea ice at a rate of almost 13% per decade, and over the past 30 years, the oldest and thickest ice in the Arctic has declined by a stunning 95%.
    ''')

    sl4=st.selectbox("Select Plot",['ALL','Annual avg. sea-ice extent','Comparison of month-wiseice coverage'])

    if sl4=="Annual avg. sea-ice extent" or sl4=="ALL":
        image = Image.open('s1.jpg')
        st.image(image, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

    if sl4=="Comparison of month-wiseice coverage" or sl4=="ALL":
        imag = Image.open('s2.jpg')
        st.image(imag, width = 1000)







if rad=="CO2 stats (choose country from below)":
    st.title("CO2 stats")
    image = Image.open('d13.jpg')
    st.image(image, width = 900)
    st.markdown('''
    Carbon dioxide is a greenhouse gas: a gas that absorbs and radiates heat. ... But increases in greenhouse gases have tipped the Earth's energy budget out of balance, trapping additional heat and raising Earth's average temperature. Carbon dioxide is the most important of Earth's long-lived greenhouse gases.\n
    As CO2 soaks up this infrared energy, it vibrates and re-emits the infrared energy back in all directions. About half of that energy goes out into space, and about half of it returns to Earth as heat, contributing to the 'greenhouse effect.
    ''')
    sl5=st.sidebar.radio("Choose country",["ALL","India","Australia","U.K","U.S.A"])
    '''\n'''
    '''\n'''
    '''\n'''
    '''\n'''
    if sl5=="India" or sl5=="ALL":
        st.header('Per capita CO₂ emissions')
        st.subheader('Carbon dioxide (CO₂) emissions from the burning of fossil fuels for energy and cement production. Land use change is not included.')
        st.markdown('''
        Annual emissions figures are often used to compare countries’ contribution to climate change. But this metric often reflects differences in population size across the world.

        To understand the ‘footprint’ of the average person in a given country, this chart shows per capita emissions.

        These figures reflect ‘production-based’ emissions, so do not correct for traded goods.

        ''')
        
        image = Image.open('p1.jpg')
        st.image(image, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Annual CO₂ emissions')
        st.subheader('Carbon dioxide (CO₂) emissions from the burning of fossil fuels for energy and cement production. Land use change is not included.')
        st.markdown('''
        A few points to keep in mind when considering this data:\n
        *These figures are based on ‘production’ or ‘territorial’ emissions (i.e. emissions from the burning of fossil fuels, or cement production within a country’s borders). It does not consider the emissions traded goods (consumption-based emissions). You find consumption-based emissions later in this country profile.
        \n*These figures look specifically at CO2 emissions – not total greenhouse gas emissions. You find total, and other greenhouse gas emissions, later in this country profile.
        \n*Annual emissions can be largely influenced by population size – we present the per capita figures above.

        ''')
        imag = Image.open('p2.jpg')
        st.image(imag, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Year-on-year change in CO₂ emissions')
        st.subheader('Absolute annual change in carbon dioxide (CO₂) emissions, measured in tonnes.')
        st.markdown('''
        This chart shows the year-on-year growth in annual CO2 emissions.

        *A positive figure indicates that the emissions in a given year were higher than the previous year.
        \n*A negative figure indicates that emissions were lower than the previous year.
        \nYear-to-year changes in emissions can vary a lot – this can create a particularly ‘noisy’ time series.
        ''')
        ima = Image.open('p3.jpg')
        st.image(ima, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Cumulative CO₂ emissions')
        st.subheader('Cumulative carbon dioxide (CO₂) emissions represents the total sum of CO₂ emissions produced from fossil fuels and cement since 1751, and is measured in tonnes. This measures CO₂ emissions from fossil fuels and cement production only – land use change is not included.')
        st.markdown('''
        When we only look at emissions produced today, we fail to recognise historical responsibility for emissions in recent decades or centuries.

        This chart shows cumulative CO2 emissions – the sum of emissions produced since 1751 to the given year. This allows us to understand how much of the total CO2 emissions to date has been emitted by a given country.
        ''')
        im = Image.open('p4.jpg')
        st.image(im, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Production vs. consumption-based CO₂ emissions, India')
        st.subheader('Annual consumption-based emissions are domestic emissions adjusted for trade. If a country imports goods the CO₂ emissions needed to produce such goods are added to its domestic emissions; if it exports goods then this is subtracted.')
        st.markdown('''
        When countries set targets, measure or compare CO2 emissions, they tend to focus on production-based emissions – CO2 emitted within a country’s own borders. However, this fails to capture emissions from traded goods – the CO2 emitted in the production of goods elsewhere, which are later imported (or the opposite: emissions from goods that are exported).

        We can estimate consumption-based CO2 emissions by correcting for trade. These emissions are shown in the interactive chart. Note that the resolution of data needed to calculate this is not available for all countries.
        ''')
        i = Image.open('p5.jpg')
        st.image(i, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Annual share of global CO₂ emissions')
        st.subheader("Each country's share of global carbon dioxide (CO₂) emissions. This is measured as each country's emissions divided by the sum of all countries' emissions in a given year plus international aviation and shipping (known as 'bunkers') and 'statistical differences' in carbon accounts.")
        st.markdown('''
        Looking at a country’s annual emissions is useful, but it can be hard to put these numbers in context of the global total. Is 10 million tonnes of CO2 large or small; what about 100 million; or 1 billion tonnes?

        This chart shows annual emissions as a percentage of the global total in a given year.
        ''')
        ii = Image.open('p6.jpg')
        st.image(ii, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Share of global cumulative CO₂ emissions, 2019')
        st.subheader("Each country or region's share of cumulative global carbon dioxide (CO₂) emissions. Cumulative emissions are calculated as the sum of annuals emissions from 1751 to a given year.")
        st.markdown('''
        Just as with annual emissions, simply presenting cumulative CO2 figures can be hard to contextualize. Has a given country’s contribution to the global total been large or small?

        This chart shows the country’s cumulative emissions as a share of global cumulative emissions.
        ''')
        iii = Image.open('p7.jpg')
        st.image(iii, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('CO₂ emissions by fuel type, India')
        st.subheader("Annual carbon dioxide (CO₂) emissions from different fuel types, measured in tonnes per year.")
        st.markdown('''
        CO2 emissions are dominated by the burning of fossil fuels for energy production, and industrial production of materials such as cement.

        What is the contribution of each fuel source to the country’s CO2 emissions?

        This interactive chart shows the breakdown of annual CO2 emissions by source: either coal, oil, gas, cement production or gas flaring. This breakdown is strongly influenced by the energy mix of a given country, and changes as a country shifts to or from a given energy source.
        ''')
        iiii = Image.open('p8.jpg')
        st.image(iiii, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''
        st.header('CO2 emissions by fuel, India')
        st.markdown('''
        The chart above allows us to see the breakdown of CO2 emissions by fuel type. But it makes it more difficult to see the absolute change in particular fuel sources over time.

        This interactive chart shows the same data – CO2 emissions from coal, oil, gas, cement and flaring – but as individual lines to see clearly how each is changing over time.
        ''')
        k = Image.open('p9.jpg')
        st.image(k, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Per capita greenhouse gas emissions')
        st.subheader("Greenhouse gas emissions – from carbon dioxide, methane, nitrous oxide, and F-gases – are summed up and measured in tonnes of carbon-dioxide equivalents (CO₂e), where “equivalent” means “having the same warming effect as CO₂ over a period of 100 years”. Emissions from land use change – which can be positive or negative – are taken into account.")
        k1 = Image.open('p10.jpg')
        st.image(k1, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Greenhouse gas emissions by sector, India, 2016')
        st.subheader("Greenhouse gas emissions are measured in tonnes of carbon dioxide-equivalents (CO₂e).")
        k2 = Image.open('p11.jpg')
        st.image(k2, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Per capita methane emissions')
        st.subheader("Per capita methane emissions are measured in tonnes of carbon-dioxide equivalents (CO2e) per person per year. This metric converts all greenhouse gases to CO2e based on their global warming potential value over a 100-year timescale.")
        k3 = Image.open('p12.jpg')
        st.image(k3, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Methane emissions by sector, India, 2016')
        st.subheader("Methane (CH₄) emissions are measured in tonnes of carbon dioxide equivalents (CO₂e) based on a 100-year global warming potential value.")
        k4 = Image.open('p13.jpg')
        st.image(k4, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Per capita nitrous oxide emissions')
        st.subheader("Per capita nitrous oxide emissions are measured in tonnes of carbon-dioxide equivalents (CO2e) per person per year. This metric converts all greenhouse gases to CO2e based on their global warming potential value over a 100-year timescale.")
        k5 = Image.open('p14.jpg')
        st.image(k5, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Nitrous oxide emissions by sector, India, 2016')
        st.subheader("Nitrous oxide (N₂O) emissions are measured in tonnes of carbon dioxide equivalents (CO₂e) based on a 100-year global warming potential value.")
        k6 = Image.open('p15.jpg')
        st.image(k6, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Energy intensity')
        st.subheader("Energy intensity is measured as primary energy consumption per unit of gross domestic product. This is measured in kilowatt-hours per 2011$ (PPP).")
        st.markdown('''
        Since energy is such a large contributor to CO2, reducing energy consumption can inevitably help to reduce emissions. However, some energy consumption is essential to human wellbeing and rising living standards.

        Energy intensity can therefore be a useful metric to monitor. Energy intensity measures the amount of energy consumed per unit of gross domestic product. It effectively measures how efficiently a country uses energy to produce a given amount of economic output. A lower energy intensity means it needs less energy per unit of GDP.
        ''')
        k7 = Image.open('p16.jpg')
        st.image(k7, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Carbon intensity of energy production')
        st.subheader("Carbon intensity of energy production is measured as the quantity of carbon dioxide emitted per unit of energy production. This is measured in kilograms of CO₂ per kilowatt-hour.")
        st.markdown('''
        Energy intensity – shown in the chart above – is one important metric to monitor whether countries are making progress in reducing emissions. The other key part of this equation is carbon intensity: the amount of CO2 emitted per unit of energy.

        We can reduce emissions by (1) using less energy; and/or (2) using lower-carbon energy.

        This metric monitors the second option. As we transition our energy mix towards lower-carbon sources (such as renewables or nuclear energy), the amount of carbon we emit per unit of energy should fall.

        This chart shows carbon intensity – measured in kilograms of CO2 emitted per kilogram of oil equivalent consumed.
        ''')
        k8 = Image.open('p17.jpg')
        st.image(k8, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Change in per capita CO₂ emissions and GDP, India')
        st.subheader("Annual consumption-based emissions are domestic emissions adjusted for trade. If a country imports goods the CO₂ emissions needed to produce such goods are added to its domestic emissions; if it exports goods then this is subtracted.")
        st.markdown('''
        To reduce emissions and achieve increasing prosperity at the same time, we have to decouple economic growth from CO2 emissions. Several countries have achieved this in recent years.

        The chart here shows whether this country has achieved this by showing the change in GDP per capita, and annual per capita CO2 emissions over time.

        We show both production-based and consumption-based emissions (for countries where this data is available). This allows us to see whether the import of production from other countries – or the export to other countries – has affected this change in emissions.
        ''')
        k9 = Image.open('p18.jpg')
        st.image(k9, width = 1000)

        
    if sl5=="Australia" or sl5=="ALL":
        st.header('Per capita CO₂ emissions')
        st.subheader('Carbon dioxide (CO₂) emissions from the burning of fossil fuels for energy and cement production. Land use change is not included.')
        st.markdown('''
        Annual emissions figures are often used to compare countries’ contribution to climate change. But this metric often reflects differences in population size across the world.

        To understand the ‘footprint’ of the average person in a given country, this chart shows per capita emissions.

        These figures reflect ‘production-based’ emissions, so do not correct for traded goods.

        ''')
        image = Image.open('a1.jpg')
        st.image(image, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Annual CO₂ emissions')
        st.subheader('Carbon dioxide (CO₂) emissions from the burning of fossil fuels for energy and cement production. Land use change is not included.')
        st.markdown('''
        A few points to keep in mind when considering this data:\n
        *These figures are based on ‘production’ or ‘territorial’ emissions (i.e. emissions from the burning of fossil fuels, or cement production within a country’s borders). It does not consider the emissions traded goods (consumption-based emissions). You find consumption-based emissions later in this country profile.
        \n*These figures look specifically at CO2 emissions – not total greenhouse gas emissions. You find total, and other greenhouse gas emissions, later in this country profile.
        \n*Annual emissions can be largely influenced by population size – we present the per capita figures above.

        ''')
        imag = Image.open('a2.jpg')
        st.image(imag, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Year-on-year change in CO₂ emissions')
        st.subheader('Absolute annual change in carbon dioxide (CO₂) emissions, measured in tonnes.')
        st.markdown('''
        This chart shows the year-on-year growth in annual CO2 emissions.

        *A positive figure indicates that the emissions in a given year were higher than the previous year.
        \n*A negative figure indicates that emissions were lower than the previous year.
        \nYear-to-year changes in emissions can vary a lot – this can create a particularly ‘noisy’ time series.
        ''')
        ima = Image.open('a3.jpg')
        st.image(ima, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Cumulative CO₂ emissions')
        st.subheader('Cumulative carbon dioxide (CO₂) emissions represents the total sum of CO₂ emissions produced from fossil fuels and cement since 1751, and is measured in tonnes. This measures CO₂ emissions from fossil fuels and cement production only – land use change is not included.')
        st.markdown('''
        When we only look at emissions produced today, we fail to recognise historical responsibility for emissions in recent decades or centuries.

        This chart shows cumulative CO2 emissions – the sum of emissions produced since 1751 to the given year. This allows us to understand how much of the total CO2 emissions to date has been emitted by a given country.
        ''')
        im = Image.open('a4.jpg')
        st.image(im, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Production vs. consumption-based CO₂ emissions, Australia')
        st.subheader('Annual consumption-based emissions are domestic emissions adjusted for trade. If a country imports goods the CO₂ emissions needed to produce such goods are added to its domestic emissions; if it exports goods then this is subtracted.')
        st.markdown('''
        When countries set targets, measure or compare CO2 emissions, they tend to focus on production-based emissions – CO2 emitted within a country’s own borders. However, this fails to capture emissions from traded goods – the CO2 emitted in the production of goods elsewhere, which are later imported (or the opposite: emissions from goods that are exported).

        We can estimate consumption-based CO2 emissions by correcting for trade. These emissions are shown in the interactive chart. Note that the resolution of data needed to calculate this is not available for all countries.
        ''')
        i = Image.open('a5.jpg')
        st.image(i, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Annual share of global CO₂ emissions')
        st.subheader("Each country's share of global carbon dioxide (CO₂) emissions. This is measured as each country's emissions divided by the sum of all countries' emissions in a given year plus international aviation and shipping (known as 'bunkers') and 'statistical differences' in carbon accounts.")
        st.markdown('''
        Looking at a country’s annual emissions is useful, but it can be hard to put these numbers in context of the global total. Is 10 million tonnes of CO2 large or small; what about 100 million; or 1 billion tonnes?

        This chart shows annual emissions as a percentage of the global total in a given year.
        ''')
        ii = Image.open('a6.jpg')
        st.image(ii, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Share of global cumulative CO₂ emissions, 2019')
        st.subheader("Each country or region's share of cumulative global carbon dioxide (CO₂) emissions. Cumulative emissions are calculated as the sum of annuals emissions from 1751 to a given year.")
        st.markdown('''
        Just as with annual emissions, simply presenting cumulative CO2 figures can be hard to contextualize. Has a given country’s contribution to the global total been large or small?

        This chart shows the country’s cumulative emissions as a share of global cumulative emissions.
        ''')
        iii = Image.open('a7.jpg')
        st.image(iii, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('CO₂ emissions by fuel type, Australia')
        st.subheader("Annual carbon dioxide (CO₂) emissions from different fuel types, measured in tonnes per year.")
        st.markdown('''
        CO2 emissions are dominated by the burning of fossil fuels for energy production, and industrial production of materials such as cement.

        What is the contribution of each fuel source to the country’s CO2 emissions?

        This interactive chart shows the breakdown of annual CO2 emissions by source: either coal, oil, gas, cement production or gas flaring. This breakdown is strongly influenced by the energy mix of a given country, and changes as a country shifts to or from a given energy source.
        ''')
        iiii = Image.open('a8.jpg')
        st.image(iiii, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''
        st.header('CO2 emissions by fuel, Australia')
        st.markdown('''
        The chart above allows us to see the breakdown of CO2 emissions by fuel type. But it makes it more difficult to see the absolute change in particular fuel sources over time.

        This interactive chart shows the same data – CO2 emissions from coal, oil, gas, cement and flaring – but as individual lines to see clearly how each is changing over time.
        ''')
        k = Image.open('a9.jpg')
        st.image(k, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Per capita greenhouse gas emissions')
        st.subheader("Greenhouse gas emissions – from carbon dioxide, methane, nitrous oxide, and F-gases – are summed up and measured in tonnes of carbon-dioxide equivalents (CO₂e), where “equivalent” means “having the same warming effect as CO₂ over a period of 100 years”. Emissions from land use change – which can be positive or negative – are taken into account.")
        k1 = Image.open('a10.jpg')
        st.image(k1, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Greenhouse gas emissions by sector, Australia, 2016')
        st.subheader("Greenhouse gas emissions are measured in tonnes of carbon dioxide-equivalents (CO₂e).")
        k2 = Image.open('a11.jpg')
        st.image(k2, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Per capita methane emissions')
        st.subheader("Per capita methane emissions are measured in tonnes of carbon-dioxide equivalents (CO2e) per person per year. This metric converts all greenhouse gases to CO2e based on their global warming potential value over a 100-year timescale.")
        k3 = Image.open('a12.jpg')
        st.image(k3, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Methane emissions by sector, Australia, 2016')
        st.subheader("Methane (CH₄) emissions are measured in tonnes of carbon dioxide equivalents (CO₂e) based on a 100-year global warming potential value.")
        k4 = Image.open('a13.jpg')
        st.image(k4, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Per capita nitrous oxide emissions')
        st.subheader("Per capita nitrous oxide emissions are measured in tonnes of carbon-dioxide equivalents (CO2e) per person per year. This metric converts all greenhouse gases to CO2e based on their global warming potential value over a 100-year timescale.")
        k5 = Image.open('a14.jpg')
        st.image(k5, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Nitrous oxide emissions by sector, Australia, 2016')
        st.subheader("Nitrous oxide (N₂O) emissions are measured in tonnes of carbon dioxide equivalents (CO₂e) based on a 100-year global warming potential value.")
        k6 = Image.open('a15.jpg')
        st.image(k6, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Energy intensity')
        st.subheader("Energy intensity is measured as primary energy consumption per unit of gross domestic product. This is measured in kilowatt-hours per 2011$ (PPP).")
        st.markdown('''
        Since energy is such a large contributor to CO2, reducing energy consumption can inevitably help to reduce emissions. However, some energy consumption is essential to human wellbeing and rising living standards.

        Energy intensity can therefore be a useful metric to monitor. Energy intensity measures the amount of energy consumed per unit of gross domestic product. It effectively measures how efficiently a country uses energy to produce a given amount of economic output. A lower energy intensity means it needs less energy per unit of GDP.
        ''')
        k7 = Image.open('a16.jpg')
        st.image(k7, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Carbon intensity of energy production')
        st.subheader("Carbon intensity of energy production is measured as the quantity of carbon dioxide emitted per unit of energy production. This is measured in kilograms of CO₂ per kilowatt-hour.")
        st.markdown('''
        Energy intensity – shown in the chart above – is one important metric to monitor whether countries are making progress in reducing emissions. The other key part of this equation is carbon intensity: the amount of CO2 emitted per unit of energy.

        We can reduce emissions by (1) using less energy; and/or (2) using lower-carbon energy.

        This metric monitors the second option. As we transition our energy mix towards lower-carbon sources (such as renewables or nuclear energy), the amount of carbon we emit per unit of energy should fall.

        This chart shows carbon intensity – measured in kilograms of CO2 emitted per kilogram of oil equivalent consumed.
        ''')
        k8 = Image.open('a17.jpg')
        st.image(k8, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Change in per capita CO₂ emissions and GDP, Australia')
        st.subheader("Annual consumption-based emissions are domestic emissions adjusted for trade. If a country imports goods the CO₂ emissions needed to produce such goods are added to its domestic emissions; if it exports goods then this is subtracted.")
        st.markdown('''
        To reduce emissions and achieve increasing prosperity at the same time, we have to decouple economic growth from CO2 emissions. Several countries have achieved this in recent years.

        The chart here shows whether this country has achieved this by showing the change in GDP per capita, and annual per capita CO2 emissions over time.

        We show both production-based and consumption-based emissions (for countries where this data is available). This allows us to see whether the import of production from other countries – or the export to other countries – has affected this change in emissions.
        ''')
        k9 = Image.open('a18.jpg')
        st.image(k9, width = 1000)



    if sl5=="U.K" or sl5=="ALL":
        st.header('Per capita CO₂ emissions')
        st.subheader('Carbon dioxide (CO₂) emissions from the burning of fossil fuels for energy and cement production. Land use change is not included.')
        st.markdown('''
        Annual emissions figures are often used to compare countries’ contribution to climate change. But this metric often reflects differences in population size across the world.

        To understand the ‘footprint’ of the average person in a given country, this chart shows per capita emissions.

        These figures reflect ‘production-based’ emissions, so do not correct for traded goods.

        ''')
        image = Image.open('k1.jpg')
        st.image(image, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Annual CO₂ emissions')
        st.subheader('Carbon dioxide (CO₂) emissions from the burning of fossil fuels for energy and cement production. Land use change is not included.')
        st.markdown('''
        A few points to keep in mind when considering this data:\n
        *These figures are based on ‘production’ or ‘territorial’ emissions (i.e. emissions from the burning of fossil fuels, or cement production within a country’s borders). It does not consider the emissions traded goods (consumption-based emissions). You find consumption-based emissions later in this country profile.
        \n*These figures look specifically at CO2 emissions – not total greenhouse gas emissions. You find total, and other greenhouse gas emissions, later in this country profile.
        \n*Annual emissions can be largely influenced by population size – we present the per capita figures above.

        ''')
        imag = Image.open('k2.jpg')
        st.image(imag, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Year-on-year change in CO₂ emissions')
        st.subheader('Absolute annual change in carbon dioxide (CO₂) emissions, measured in tonnes.')
        st.markdown('''
        This chart shows the year-on-year growth in annual CO2 emissions.

        *A positive figure indicates that the emissions in a given year were higher than the previous year.
        \n*A negative figure indicates that emissions were lower than the previous year.
        \nYear-to-year changes in emissions can vary a lot – this can create a particularly ‘noisy’ time series.
        ''')
        ima = Image.open('k3.jpg')
        st.image(ima, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Cumulative CO₂ emissions')
        st.subheader('Cumulative carbon dioxide (CO₂) emissions represents the total sum of CO₂ emissions produced from fossil fuels and cement since 1751, and is measured in tonnes. This measures CO₂ emissions from fossil fuels and cement production only – land use change is not included.')
        st.markdown('''
        When we only look at emissions produced today, we fail to recognise historical responsibility for emissions in recent decades or centuries.

        This chart shows cumulative CO2 emissions – the sum of emissions produced since 1751 to the given year. This allows us to understand how much of the total CO2 emissions to date has been emitted by a given country.
        ''')
        im = Image.open('k4.jpg')
        st.image(im, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Production vs. consumption-based CO₂ emissions, U.K')
        st.subheader('Annual consumption-based emissions are domestic emissions adjusted for trade. If a country imports goods the CO₂ emissions needed to produce such goods are added to its domestic emissions; if it exports goods then this is subtracted.')
        st.markdown('''
        When countries set targets, measure or compare CO2 emissions, they tend to focus on production-based emissions – CO2 emitted within a country’s own borders. However, this fails to capture emissions from traded goods – the CO2 emitted in the production of goods elsewhere, which are later imported (or the opposite: emissions from goods that are exported).

        We can estimate consumption-based CO2 emissions by correcting for trade. These emissions are shown in the interactive chart. Note that the resolution of data needed to calculate this is not available for all countries.
        ''')
        i = Image.open('k5.jpg')
        st.image(i, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Annual share of global CO₂ emissions')
        st.subheader("Each country's share of global carbon dioxide (CO₂) emissions. This is measured as each country's emissions divided by the sum of all countries' emissions in a given year plus international aviation and shipping (known as 'bunkers') and 'statistical differences' in carbon accounts.")
        st.markdown('''
        Looking at a country’s annual emissions is useful, but it can be hard to put these numbers in context of the global total. Is 10 million tonnes of CO2 large or small; what about 100 million; or 1 billion tonnes?

        This chart shows annual emissions as a percentage of the global total in a given year.
        ''')
        ii = Image.open('k6.jpg')
        st.image(ii, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Share of global cumulative CO₂ emissions, 2019')
        st.subheader("Each country or region's share of cumulative global carbon dioxide (CO₂) emissions. Cumulative emissions are calculated as the sum of annuals emissions from 1751 to a given year.")
        st.markdown('''
        Just as with annual emissions, simply presenting cumulative CO2 figures can be hard to contextualize. Has a given country’s contribution to the global total been large or small?

        This chart shows the country’s cumulative emissions as a share of global cumulative emissions.
        ''')
        iii = Image.open('k7.jpg')
        st.image(iii, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('CO₂ emissions by fuel type, U.K')
        st.subheader("Annual carbon dioxide (CO₂) emissions from different fuel types, measured in tonnes per year.")
        st.markdown('''
        CO2 emissions are dominated by the burning of fossil fuels for energy production, and industrial production of materials such as cement.

        What is the contribution of each fuel source to the country’s CO2 emissions?

        This interactive chart shows the breakdown of annual CO2 emissions by source: either coal, oil, gas, cement production or gas flaring. This breakdown is strongly influenced by the energy mix of a given country, and changes as a country shifts to or from a given energy source.
        ''')
        iiii = Image.open('k8.jpg')
        st.image(iiii, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''
        st.header('CO2 emissions by fuel, U.K')
        st.markdown('''
        The chart above allows us to see the breakdown of CO2 emissions by fuel type. But it makes it more difficult to see the absolute change in particular fuel sources over time.

        This interactive chart shows the same data – CO2 emissions from coal, oil, gas, cement and flaring – but as individual lines to see clearly how each is changing over time.
        ''')
        k = Image.open('k9.jpg')
        st.image(k, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Per capita greenhouse gas emissions')
        st.subheader("Greenhouse gas emissions – from carbon dioxide, methane, nitrous oxide, and F-gases – are summed up and measured in tonnes of carbon-dioxide equivalents (CO₂e), where “equivalent” means “having the same warming effect as CO₂ over a period of 100 years”. Emissions from land use change – which can be positive or negative – are taken into account.")
        k1 = Image.open('k10.jpg')
        st.image(k1, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Greenhouse gas emissions by sector, U.K, 2016')
        st.subheader("Greenhouse gas emissions are measured in tonnes of carbon dioxide-equivalents (CO₂e).")
        k2 = Image.open('k11.jpg')
        st.image(k2, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Per capita methane emissions')
        st.subheader("Per capita methane emissions are measured in tonnes of carbon-dioxide equivalents (CO2e) per person per year. This metric converts all greenhouse gases to CO2e based on their global warming potential value over a 100-year timescale.")
        k3 = Image.open('k12.jpg')
        st.image(k3, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Methane emissions by sector, U.K, 2016')
        st.subheader("Methane (CH₄) emissions are measured in tonnes of carbon dioxide equivalents (CO₂e) based on a 100-year global warming potential value.")
        k4 = Image.open('k13.jpg')
        st.image(k4, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Per capita nitrous oxide emissions')
        st.subheader("Per capita nitrous oxide emissions are measured in tonnes of carbon-dioxide equivalents (CO2e) per person per year. This metric converts all greenhouse gases to CO2e based on their global warming potential value over a 100-year timescale.")
        k5 = Image.open('k14.jpg')
        st.image(k5, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Nitrous oxide emissions by sector, U.K, 2016')
        st.subheader("Nitrous oxide (N₂O) emissions are measured in tonnes of carbon dioxide equivalents (CO₂e) based on a 100-year global warming potential value.")
        k6 = Image.open('k15.jpg')
        st.image(k6, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Energy intensity')
        st.subheader("Energy intensity is measured as primary energy consumption per unit of gross domestic product. This is measured in kilowatt-hours per 2011$ (PPP).")
        st.markdown('''
        Since energy is such a large contributor to CO2, reducing energy consumption can inevitably help to reduce emissions. However, some energy consumption is essential to human wellbeing and rising living standards.

        Energy intensity can therefore be a useful metric to monitor. Energy intensity measures the amount of energy consumed per unit of gross domestic product. It effectively measures how efficiently a country uses energy to produce a given amount of economic output. A lower energy intensity means it needs less energy per unit of GDP.
        ''')
        k7 = Image.open('k16.jpg')
        st.image(k7, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Carbon intensity of energy production')
        st.subheader("Carbon intensity of energy production is measured as the quantity of carbon dioxide emitted per unit of energy production. This is measured in kilograms of CO₂ per kilowatt-hour.")
        st.markdown('''
        Energy intensity – shown in the chart above – is one important metric to monitor whether countries are making progress in reducing emissions. The other key part of this equation is carbon intensity: the amount of CO2 emitted per unit of energy.

        We can reduce emissions by (1) using less energy; and/or (2) using lower-carbon energy.

        This metric monitors the second option. As we transition our energy mix towards lower-carbon sources (such as renewables or nuclear energy), the amount of carbon we emit per unit of energy should fall.

        This chart shows carbon intensity – measured in kilograms of CO2 emitted per kilogram of oil equivalent consumed.
        ''')
        k8 = Image.open('k17.jpg')
        st.image(k8, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Change in per capita CO₂ emissions and GDP, U.K')
        st.subheader("Annual consumption-based emissions are domestic emissions adjusted for trade. If a country imports goods the CO₂ emissions needed to produce such goods are added to its domestic emissions; if it exports goods then this is subtracted.")
        st.markdown('''
        To reduce emissions and achieve increasing prosperity at the same time, we have to decouple economic growth from CO2 emissions. Several countries have achieved this in recent years.

        The chart here shows whether this country has achieved this by showing the change in GDP per capita, and annual per capita CO2 emissions over time.

        We show both production-based and consumption-based emissions (for countries where this data is available). This allows us to see whether the import of production from other countries – or the export to other countries – has affected this change in emissions.
        ''')
        k9 = Image.open('k18.jpg')
        st.image(k9, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

    if sl5=="U.S.A" or sl5=="ALL":
        st.header('Per capita CO₂ emissions')
        st.subheader('Carbon dioxide (CO₂) emissions from the burning of fossil fuels for energy and cement production. Land use change is not included.')
        st.markdown('''
        Annual emissions figures are often used to compare countries’ contribution to climate change. But this metric often reflects differences in population size across the world.

        To understand the ‘footprint’ of the average person in a given country, this chart shows per capita emissions.

        These figures reflect ‘production-based’ emissions, so do not correct for traded goods.

        ''')
        image = Image.open('u1.jpg')
        st.image(image, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Annual CO₂ emissions')
        st.subheader('Carbon dioxide (CO₂) emissions from the burning of fossil fuels for energy and cement production. Land use change is not included.')
        st.markdown('''
        A few points to keep in mind when considering this data:\n
        *These figures are based on ‘production’ or ‘territorial’ emissions (i.e. emissions from the burning of fossil fuels, or cement production within a country’s borders). It does not consider the emissions traded goods (consumption-based emissions). You find consumption-based emissions later in this country profile.
        \n*These figures look specifically at CO2 emissions – not total greenhouse gas emissions. You find total, and other greenhouse gas emissions, later in this country profile.
        \n*Annual emissions can be largely influenced by population size – we present the per capita figures above.

        ''')
        imag = Image.open('u2.jpg')
        st.image(imag, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Year-on-year change in CO₂ emissions')
        st.subheader('Absolute annual change in carbon dioxide (CO₂) emissions, measured in tonnes.')
        st.markdown('''
        This chart shows the year-on-year growth in annual CO2 emissions.

        *A positive figure indicates that the emissions in a given year were higher than the previous year.
        \n*A negative figure indicates that emissions were lower than the previous year.
        \nYear-to-year changes in emissions can vary a lot – this can create a particularly ‘noisy’ time series.
        ''')
        ima = Image.open('u3.jpg')
        st.image(ima, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Cumulative CO₂ emissions')
        st.subheader('Cumulative carbon dioxide (CO₂) emissions represents the total sum of CO₂ emissions produced from fossil fuels and cement since 1751, and is measured in tonnes. This measures CO₂ emissions from fossil fuels and cement production only – land use change is not included.')
        st.markdown('''
        When we only look at emissions produced today, we fail to recognise historical responsibility for emissions in recent decades or centuries.

        This chart shows cumulative CO2 emissions – the sum of emissions produced since 1751 to the given year. This allows us to understand how much of the total CO2 emissions to date has been emitted by a given country.
        ''')
        im = Image.open('u4.jpg')
        st.image(im, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Production vs. consumption-based CO₂ emissions, U.S.A')
        st.subheader('Annual consumption-based emissions are domestic emissions adjusted for trade. If a country imports goods the CO₂ emissions needed to produce such goods are added to its domestic emissions; if it exports goods then this is subtracted.')
        st.markdown('''
        When countries set targets, measure or compare CO2 emissions, they tend to focus on production-based emissions – CO2 emitted within a country’s own borders. However, this fails to capture emissions from traded goods – the CO2 emitted in the production of goods elsewhere, which are later imported (or the opposite: emissions from goods that are exported).

        We can estimate consumption-based CO2 emissions by correcting for trade. These emissions are shown in the interactive chart. Note that the resolution of data needed to calculate this is not available for all countries.
        ''')
        i = Image.open('u5.jpg')
        st.image(i, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Annual share of global CO₂ emissions')
        st.subheader("Each country's share of global carbon dioxide (CO₂) emissions. This is measured as each country's emissions divided by the sum of all countries' emissions in a given year plus international aviation and shipping (known as 'bunkers') and 'statistical differences' in carbon accounts.")
        st.markdown('''
        Looking at a country’s annual emissions is useful, but it can be hard to put these numbers in context of the global total. Is 10 million tonnes of CO2 large or small; what about 100 million; or 1 billion tonnes?

        This chart shows annual emissions as a percentage of the global total in a given year.
        ''')
        ii = Image.open('u6.jpg')
        st.image(ii, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Share of global cumulative CO₂ emissions, 2019')
        st.subheader("Each country or region's share of cumulative global carbon dioxide (CO₂) emissions. Cumulative emissions are calculated as the sum of annuals emissions from 1751 to a given year.")
        st.markdown('''
        Just as with annual emissions, simply presenting cumulative CO2 figures can be hard to contextualize. Has a given country’s contribution to the global total been large or small?

        This chart shows the country’s cumulative emissions as a share of global cumulative emissions.
        ''')
        iii = Image.open('u7.jpg')
        st.image(iii, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('CO₂ emissions by fuel type, U.S.A')
        st.subheader("Annual carbon dioxide (CO₂) emissions from different fuel types, measured in tonnes per year.")
        st.markdown('''
        CO2 emissions are dominated by the burning of fossil fuels for energy production, and industrial production of materials such as cement.

        What is the contribution of each fuel source to the country’s CO2 emissions?

        This interactive chart shows the breakdown of annual CO2 emissions by source: either coal, oil, gas, cement production or gas flaring. This breakdown is strongly influenced by the energy mix of a given country, and changes as a country shifts to or from a given energy source.
        ''')
        iiii = Image.open('u8.jpg')
        st.image(iiii, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''
        st.header('CO2 emissions by fuel, U.S.A')
        st.markdown('''
        The chart above allows us to see the breakdown of CO2 emissions by fuel type. But it makes it more difficult to see the absolute change in particular fuel sources over time.

        This interactive chart shows the same data – CO2 emissions from coal, oil, gas, cement and flaring – but as individual lines to see clearly how each is changing over time.
        ''')
        k = Image.open('u9.jpg')
        st.image(k, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Per capita greenhouse gas emissions')
        st.subheader("Greenhouse gas emissions – from carbon dioxide, methane, nitrous oxide, and F-gases – are summed up and measured in tonnes of carbon-dioxide equivalents (CO₂e), where “equivalent” means “having the same warming effect as CO₂ over a period of 100 years”. Emissions from land use change – which can be positive or negative – are taken into account.")
        k1 = Image.open('u10.jpg')
        st.image(k1, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Greenhouse gas emissions by sector, U.S.A, 2016')
        st.subheader("Greenhouse gas emissions are measured in tonnes of carbon dioxide-equivalents (CO₂e).")
        k2 = Image.open('u11.jpg')
        st.image(k2, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Per capita methane emissions')
        st.subheader("Per capita methane emissions are measured in tonnes of carbon-dioxide equivalents (CO2e) per person per year. This metric converts all greenhouse gases to CO2e based on their global warming potential value over a 100-year timescale.")
        k3 = Image.open('u12.jpg')
        st.image(k3, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Methane emissions by sector, U.S.A, 2016')
        st.subheader("Methane (CH₄) emissions are measured in tonnes of carbon dioxide equivalents (CO₂e) based on a 100-year global warming potential value.")
        k4 = Image.open('u13.jpg')
        st.image(k4, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Per capita nitrous oxide emissions')
        st.subheader("Per capita nitrous oxide emissions are measured in tonnes of carbon-dioxide equivalents (CO2e) per person per year. This metric converts all greenhouse gases to CO2e based on their global warming potential value over a 100-year timescale.")
        k5 = Image.open('u14.jpg')
        st.image(k5, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Nitrous oxide emissions by sector, U.S.A, 2016')
        st.subheader("Nitrous oxide (N₂O) emissions are measured in tonnes of carbon dioxide equivalents (CO₂e) based on a 100-year global warming potential value.")
        k6 = Image.open('u15.jpg')
        st.image(k6, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''


        st.header('Energy intensity')
        st.subheader("Energy intensity is measured as primary energy consumption per unit of gross domestic product. This is measured in kilowatt-hours per 2011$ (PPP).")
        st.markdown('''
        Since energy is such a large contributor to CO2, reducing energy consumption can inevitably help to reduce emissions. However, some energy consumption is essential to human wellbeing and rising living standards.

        Energy intensity can therefore be a useful metric to monitor. Energy intensity measures the amount of energy consumed per unit of gross domestic product. It effectively measures how efficiently a country uses energy to produce a given amount of economic output. A lower energy intensity means it needs less energy per unit of GDP.
        ''')
        k7 = Image.open('u16.jpg')
        st.image(k7, width = 1000)
        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Carbon intensity of energy production')
        st.subheader("Carbon intensity of energy production is measured as the quantity of carbon dioxide emitted per unit of energy production. This is measured in kilograms of CO₂ per kilowatt-hour.")
        st.markdown('''
        Energy intensity – shown in the chart above – is one important metric to monitor whether countries are making progress in reducing emissions. The other key part of this equation is carbon intensity: the amount of CO2 emitted per unit of energy.

        We can reduce emissions by (1) using less energy; and/or (2) using lower-carbon energy.

        This metric monitors the second option. As we transition our energy mix towards lower-carbon sources (such as renewables or nuclear energy), the amount of carbon we emit per unit of energy should fall.

        This chart shows carbon intensity – measured in kilograms of CO2 emitted per kilogram of oil equivalent consumed.
        ''')
        k8 = Image.open('u17.jpg')
        st.image(k8, width = 1000)

        '''\n'''
        '''\n'''
        '''\n'''
        '''\n'''

        st.header('Change in per capita CO₂ emissions and GDP, U.S.A')
        st.subheader("Annual consumption-based emissions are domestic emissions adjusted for trade. If a country imports goods the CO₂ emissions needed to produce such goods are added to its domestic emissions; if it exports goods then this is subtracted.")
        st.markdown('''
        To reduce emissions and achieve increasing prosperity at the same time, we have to decouple economic growth from CO2 emissions. Several countries have achieved this in recent years.

        The chart here shows whether this country has achieved this by showing the change in GDP per capita, and annual per capita CO2 emissions over time.

        We show both production-based and consumption-based emissions (for countries where this data is available). This allows us to see whether the import of production from other countries – or the export to other countries – has affected this change in emissions.
        ''')
        k9 = Image.open('u18.jpg')
        st.image(k9, width = 1000)








if rad=="Indian statewise electricity stats":
    st.title('ELECTRICITY CONSUMPTION (Indian statewise)')
    image = Image.open('d4.jpg')
    st.image(image, width = 800)
    st.markdown(""" 
    Electricity consumption according to Indian states and union territories
    """)

    @st.cache(allow_output_mutation=True)
    def load():
        Data1 = pd.read_csv("dataset_tk.csv")
        Data2 = pd.read_csv("long_data_.csv")
        #Data2
        Data1.isnull().sum()
        Data2.dropna(inplace = True)
        return Data1, Data2
    Data1, Data2=load()


    mean_temprature = Data1.mean().sort_values(ascending=False).reset_index().rename(columns = {"index": "state", 0 : "avg_consumption"})
    state_code = ['MH', 'GJ ', 'UP', 'TN', 'RJ', 'MP', 'KA', 'TG', 'AP', 'PB', 'WB', 'HR', 'CT', 'DL', 'BR', 'OR', 'KL', 'J&K', 'UK', 'HP', 'AS', 'JH', 'DNH', 'GA', 'PY', 'ML', 'CH', 'TR', 'MN', 'NL', 'AR', 'MZ', 'SK']
    mean_temprature.state = state_code

    sns.barplot(x= "avg_consumption", y = "state", data = mean_temprature)
    sns.set(rc={'figure.figsize':(11.7,4)})
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()


    #Data2.isnull().sum()
    Data2['Dates'] = pd.to_datetime(Data2.Dates, dayfirst=True)
    sns.barplot(x="Usage", y="States", data=Data2)
    sns.set(rc={'figure.figsize':(8,8.27)})
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
