# World Time - an app to check the time of any country/region of the world (UN recognised/UN member states countries)
# Note: This program does not account for DST (Daylight Saving Time) and does not update mutliple timezone countries realtime (i am too stupid to implement it)
# Country images made by Freepik from www.flaticon.com


# import statements
import customtkinter as ctk
from PIL import Image
from datetime import datetime, timedelta 

# window settings
app = ctk.CTk()
ctk.set_appearance_mode("dark")
app.configure(bg='#2f3030')
app.geometry("600x400")
app.title("World Time - Computer Project")
app.iconbitmap("images/icon.ico")

# window layout
app.columnconfigure((0, 1, 2, 3, 4), weight = 1, uniform = "uniform")
app.rowconfigure((0, 1, 2 , 3), weight = 1, uniform = "uniform")
app.rowconfigure((4, 5, 6, 7, 8, 9), weight = 2, uniform = "uniform")

# logo
logo = ctk.CTkImage(dark_image=Image.open("images/logo.png"), size = (100, 100))

# top text
main_title = ctk.CTkLabel(app, text="World Time", fg_color="#394cdb", text_color="white", font=("Consolas", 40), padx = 20, pady = 20, corner_radius = 20)
main_title.grid(column = 2, row = 0,columnspan = 1, pady = (10, 0),)

side_text = ctk.CTkLabel(app, text=" - a global time checker app", text_color="white", font=("Consolas", 25))
side_text.grid(column = 3, row = 0,pady = (10, 0), sticky = "nws")

logo_label = ctk.CTkLabel(app, text = "", image = logo)
logo_label.grid(column = 4, row = 0, columnspan = 1, rowspan = 2, sticky = "ne", padx = (0, 30), pady=(10, 0))

prompt_text = ctk.CTkLabel(app, text="Select a country:", text_color="#46a7e8", font=("Consolas", 20))
prompt_text.grid(column = 2, row = 1, columnspan = 1, sticky = "news", pady = (20, 0))

# country chooser
countries_optionmenu = ctk.CTkOptionMenu(app, width = 400, height = 40, dropdown_hover_color = "#5c5c5c",
dropdown_text_color="white", dropdown_font= (("Consolas", 20)), fg_color = "#51626b" , dropdown_fg_color="#2c2f33", font=("Consolas", 20),
values =  [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia',
    'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
    'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
    'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia',
    'Comoros','Costa Rica', 'Côte d\'Ivoire', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Democratic Republic of the Congo','Denmark', 'Djibouti', 'Dominica',
    'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini',
    'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada',
    'Guatemala', 'Guinea', 'Guinea Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia',
    'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati',
    'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
    'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
    'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro',
    'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger',
    'Nigeria', 'North Korea', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea',
    'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar','Republic of the Congo', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis',
    'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
    'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
    'South Africa', 'South Korea','South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria',
    'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
    'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay',
    'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
])




countries_optionmenu.grid(column = 2, row = 2,columnspan = 1)
countries_optionmenu.set("")

# all countries' info
single_timezone_countries_info = {
'Afghanistan': (4.5, 'Afghanistan Time (AFT)'),
'Albania': (1, 'Central European Time (CET)'),
'Algeria': (1, 'Central European Time (CET)'),
'Andorra': (1, 'Central European Time (CET)'),
'Angola': (1, 'Central Africa Time (CAT)'),
'Antigua and Barbuda': (-4, 'Atlantic Standard Time (AST)'),
'Argentina': (-3, 'Argentina Time (ART)'),
'Armenia': (4, 'Armenia Time (AMT)'),
'Austria': (1, 'Central European Time (CET)'),
'Azerbaijan': (4, 'Azerbaijan Time (AZT)'),
'Bahamas': (-5, 'Eastern Standard Time (EST)'),
'Bahrain': (3, 'Arabian Standard Time (AST)'),
'Bangladesh': (6, 'Bangladesh Time (BST)'),
'Barbados': (-4, 'Atlantic Standard Time (AST)'),
'Belarus': (3, 'Eastern European Time (EET)'),
'Belgium': (1, 'Central European Time (CET)'),
'Belize': (-6, 'Central Standard Time (CST)'),
'Benin': (1, 'West Africa Time (WAT)'),
'Bhutan': (6, 'Bhutan Time (BTT)'),
'Bolivia': (-4, 'Bolivia Time (BOT)'),
'Bosnia and Herzegovina': (1, 'Central European Time (CET)'),
'Botswana': (2, 'Central Africa Time (CAT)'),
'Brunei': (8, 'Brunei Time (BNT)'),
'Bulgaria': (2, 'Eastern European Time (EET)'),
'Burkina Faso': (0, 'Greenwich Mean Time (GMT)'),
'Burundi': (2, 'Central Africa Time (CAT)'),
'Cabo Verde': (-1, 'Cape Verde Time (CVT)'),
'Cambodia': (7, 'Indochina Time (ICT)'),
'Cameroon': (1, 'West Africa Time (WAT)'),
'Central African Republic': (1, 'West Africa Time (WAT)'),
'Chad': (1, 'West Africa Time (WAT)'),
'Chile': (-3, 'Chile Time (CLT)'),
'China': (8, 'China Standard Time (CST)'),
'Colombia': (-5, 'Colombia Time (COT)'),
'Comoros': (3, 'East Africa Time (EAT)'),
'Costa Rica': (-6, 'Central Standard Time (CST)'),
'Côte d\'Ivoire':(0, 'Greenwich Mean Time (GMT)'),
'Croatia': (1, 'Central European Time (CET)'),
'Cuba': (-5, 'Cuba Standard Time (CST)'),
'Cyprus': (2, 'Eastern European Time (EET)'),
'Czech Republic': (1, 'Central European Time (CET)'),
'Denmark': (1, 'Central European Time (CET)'),
'Djibouti': (3, 'East Africa Time (EAT)'),
'Dominica': (-4, 'Atlantic Standard Time (AST)'),
'Dominican Republic': (-4, 'Atlantic Standard Time (AST)'),
'Ecuador': (-5, 'Ecuador Time (ECT)'),
'Egypt': (2, 'Eastern European Time (EET)'),
'El Salvador': (-6, 'Central Standard Time (CST)'),
'Equatorial Guinea': (1, 'West Africa Time (WAT)'),
'Eritrea': (3, 'East Africa Time (EAT)'),
'Estonia': (2, 'Eastern European Time (EET)'),
'Eswatini': (2, 'Central Africa Time (CAT)'),
'Ethiopia': (3, 'East Africa Time (EAT)'),
'Fiji': (12, 'Fiji Time (FJT)'),
'Finland': (2, 'Eastern European Time (EET)'),
'France': (1, 'Central European Time (CET)'),
'Gabon': (1, 'West Africa Time (WAT)'),
'Gambia': (0, 'Greenwich Mean Time (GMT)'),
'Georgia': (4, 'Georgia Time (GET)'),
'Germany': (1, 'Central European Time (CET)'),
'Ghana': (0, 'Greenwich Mean Time (GMT)'),
'Greece': (2, 'Eastern European Time (EET)'),
'Grenada': (-4, 'Atlantic Standard Time (AST)'),
'Guatemala': (-6, 'Central Standard Time (CST)'),
'Guinea': (0, 'Greenwich Mean Time (GMT)'),
'Guinea Bissau': (0, 'Greenwich Mean Time (GMT)'),
'Guyana': (-4, 'Guyana Time (GYT)'),
'Haiti': (-5, 'Eastern Standard Time (EST)'),
'Honduras': (-6, 'Central Standard Time (CST)'),
'Hungary': (1, 'Central European Time (CET)'),
'Iceland': (0, 'Greenwich Mean Time (GMT)'),
'India': (5.5, 'Indian Standard Time (IST)'),
'Iran': (3.5, 'Iran Time (IRST)'),
'Iraq': (3, 'Arabian Standard Time (AST)'),
'Ireland': (0, 'Greenwich Mean Time (GMT)'),
'Israel': (2, 'Israel Standard Time (IST)'),
'Italy': (1, 'Central European Time (CET)'),
'Jamaica': (-5, 'Eastern Standard Time (EST)'),
'Japan': (9, 'Japan Standard Time (JST)'),
'Jordan': (2, 'Eastern European Time (EET)'),
'Kenya': (3, 'East Africa Time (EAT)'),
'Kuwait': (3, 'Arabian Standard Time (AST)'),
'Kyrgyzstan': (6, 'Kyrgyzstan Time (KGT)'),
'Laos': (7, 'Indochina Time (ICT)'),
'Latvia': (2, 'Eastern European Time (EET)'),
'Lebanon': (2, 'Eastern European Time (EET)'),
'Lesotho': (2, 'Central Africa Time (CAT)'),
'Liberia': (0, 'Greenwich Mean Time (GMT)'),
'Libya': (2, 'Eastern European Time (EET)'),
'Liechtenstein': (1, 'Central European Time (CET)'),
'Lithuania': (2, 'Eastern European Time (EET)'),
'Luxembourg': (1, 'Central European Time (CET)'),
'Madagascar': (3, 'East Africa Time (EAT)'),
'Malawi': (2, 'Central Africa Time (CAT)'),
'Malaysia': (8, 'Malaysia Time (MYT)'),
'Maldives': (5, 'Maldives Time (MVT)'),
'Mali': (0, 'Greenwich Mean Time (GMT)'),
'Malta': (1, 'Central European Time (CET)'),
'Marshall Islands':  (12, 'Marshall Islands Time (MHT)'),
'Mauritania': (0, 'Greenwich Mean Time (GMT)'),
'Mauritius': (4, 'Mauritius Time (MUT)'),
'Moldova': (2, 'Eastern European Time (EET)'),
'Monaco': (1, 'Central European Time (CET)'),
'Montenegro': (1, 'Central European Time (CET)'),
'Morocco': (0, 'Greenwich Mean Time (GMT)'),
'Mozambique': (2, 'Central Africa Time (CAT)'),
'Myanmar': (6.5, 'Myanmar Time (MMT)'),
'Namibia': (2, 'Central Africa Time (CAT)'),
'Nauru': (12, 'Nauru Time (NRT)'),
'Nepal': (5.75, 'Nepal Time (NPT)'),
'Netherlands': (1, 'Central European Time (CET)'),
'Nicaragua': (-6, 'Central Standard Time (CST)'),
'Niger': (1, 'West Africa Time (WAT)'),
'Nigeria': (1, 'West Africa Time (WAT)'),
'North Korea': (9, 'Korea Standard Time (KST)'),
'North Macedonia': (1, 'Central European Time (CET)'),
'Norway': (1, 'Central European Time (CET)'),
'Oman': (4, 'Gulf Standard Time (GST)'),
'Pakistan': (5, 'Pakistan Standard Time (PKT)'),
'Palau': (9, 'Palau Time (PWT)'),
'Palestine': (9, 'Eastern European Time (EET)'),
'Panama': (-5, 'Eastern Standard Time (EST)'),
'Paraguay': (-4, 'Paraguay Time (PYT)'),
'Peru': (-5, 'Peru Time (PET)'),
'Philippines': (8, 'Philippine Time (PHT)'),
'Poland': (1, 'Central European Time (CET)'),
'Portugal': (0, 'Greenwich Mean Time (GMT)'),
'Qatar': (3, 'Arabian Standard Time (AST)'),
'Republic of the Congo': (1, 'West Africa Time (WAT)'),
'Romania': (2, 'Eastern European Time (EET)'),
'Rwanda': (2, 'Central Africa Time (CAT)'),
'Saint Kitts and Nevis': (-4, 'Atlantic Standard Time (AST)'),
'Saint Lucia': (-4, 'Atlantic Standard Time (AST)'),
'Saint Vincent and the Grenadines': (-4, 'Atlantic Standard Time (AST)'),
'Samoa': (13, 'Samoa Time (WSST)'),
'San Marino': (1, 'Central European Time (CET)'),
'Sao Tome and Principe': (0, 'Greenwich Mean Time (GMT)'),
'Saudi Arabia': (3, 'Arabian Standard Time (AST)'),
'Senegal': (0, 'Greenwich Mean Time (GMT)'),
'Serbia': (1, 'Central European Time (CET)'),
'Seychelles': (4, 'Seychelles Time (SCT)'),
'Sierra Leone': (0, 'Greenwich Mean Time (GMT)'),
'Singapore': (8, 'Singapore Time (SGT)'),
'Slovakia': (1, 'Central European Time (CET)'),
'Slovenia': (1, 'Central European Time (CET)'),
'Solomon Islands': (11, 'Solomon Islands Time (SBT)'),
'Somalia': (3, 'East Africa Time (EAT)'),
'South Africa': (2, 'South Africa Standard Time (SAST)'),
'South Korea': (9, 'Korea Standard Time (KST)'),
'South Sudan': (3, 'East Africa Time (EAT)'),
'Spain': (1, 'Central European Time (CET)'),
'Sri Lanka': (5.5, 'Sri Lanka Time (SLT)'),
'Sudan': (2, 'Central Africa Time (CAT)'),
'Suriname': (-3, 'Suriname Time (SRT)'),
'Sweden': (1, 'Central European Time (CET)'),
'Switzerland': (1, 'Central European Time (CET)'),
'Syria': (2, 'Eastern European Time (EET)'),
'Tajikistan': (5, 'Tajikistan Time (TJT)'),
'Tanzania': (3, 'East Africa Time (EAT)'),
'Thailand': (7, 'Indochina Time (ICT)'),
'Timor-Leste': (9, 'Timor Time (TLT)'),
'Togo': (0, 'Greenwich Mean Time (GMT)'),
'Tonga': (13, 'Tonga Time (TOT)'),
'Trinidad and Tobago': (-4, 'Atlantic Standard Time (AST)'),
'Tunisia': (1, 'Central European Time (CET)'),
'Turkey': (3, 'Turkey Time (TRT)'),
'Turkmenistan': (5, 'Turkmenistan Time (TMT)'),
'Tuvalu': (12, 'Tuvalu Time (TVT)'),
'Uganda': (3, 'East Africa Time (EAT)'),
'Ukraine': (2, 'Eastern European Time (EET)'),
'United Arab Emirates': (4, 'Gulf Standard Time (GST)'),
'United Kingdom': (0, 'Greenwich Mean Time (GMT)'),
'Uruguay': (-3, 'Uruguay Time (UYT)'),
'Uzbekistan': (5, 'Uzbekistan Time (UZT)'),
'Vanuatu': (11, 'Vanuatu Time (VUT)'),
'Vatican City': (1, 'Central European Time (CET)'),
'Venezuela': (-4, 'Venezuelan Standard Time (VET)'),
'Vietnam': (7, 'Indochina Time (ICT)'),
'Yemen': (3, 'Arabian Standard Time (AST)'),
'Zambia': (2, 'Central Africa Time (CAT)'),
'Zimbabwe': (2, 'Central Africa Time (CAT)')
}

multiple_timezone_countries_info = {
'Australia': {
        'Western Australia': (8, 'Australian Western Standard Time (AWST)'),
        'Northern Territory': (9.5, 'Australian Central Standard Time (ACST)'),
        'South Australia': (9.5, 'Australian Central Standard Time (ACST)'),
        'Queensland': (10, 'Australian Eastern Standard Time (AEST)'),
        'New South Wales': (11, 'Australian Eastern Standard Time (AEST)'),
        'Australian Capital Territory': (11, 'Australian Eastern Standard Time (AEST)'),
        'Victoria': (11, 'Australian Eastern Standard Time (AEST)'),
        'Cocos Islands': (6.5, 'Australian Eastern Standard Time (AEST)'),
        'Christmas Island': (7, 'Christmas Island Time (CXT)'),
        'Norfolk Island': (12, 'Norfolk Island (NFT)')
},
'Brazil': {
        'Brasília': (-3, 'Brasília Time (BRT)'),
        'Rio de Janeiro': (-3, 'Brasília Time (BRT)'),
        'São Paulo': (-3, 'Brasília Time (BRT)'),
        'Manaus': (-4, 'Amazon Time (AMT)'),
        'Acre': (-5, 'Acre Time (ACT)')
},
'Canada': {
        'Ontario': (-5, 'Eastern Standard Time (EST)'),
        'Manitoba': (-6, 'Central Standard Time (CST)'),
        'Alberta': (-7, 'Mountain Standard Time (MST)'),
        'British Columbia': (-8, 'Pacific Standard Time (PST)'),
        'Newfoundland and Labrador': (-3.5, 'Newfoundland Standard Time (NST)'),
        'Nova Scotia': (-4, 'Atlantic Standard Time (AST)')
},
'Democratic Republic of the Congo': {
        'Kinshasa': (1, 'West Africa Time (WAT)'),
        'Maniema': (2, 'Central Africa Time (CAT)')
},
'Indonesia': {
        'Western Indonesia': (7, 'Western Indonesia Time (WIB)'),
        'Central Indonesia': (8, 'Central Indonesia Time (WITA)'),
        'Eastern Indonesia': (9, 'Eastern Indonesia Time (WIT)')
},
'Kazakhstan': {
        'Western Kazakhstan': (5, 'Western Kazakhstan Time (WKT)'),
        'Eastern Kazakhstan': (6, 'Eastern Kazakhstan Time (EKT)')
},
'Kiribati': {
        'Gilbert Islands': (12, 'Gilbert Islands Time (GILT)'),
        'Phoenix Islands': (13, 'Phoenix Islands Time (PHOT)'),
        'Line Islands': (14, 'Line Islands Time (LINT)')
},
'Mexico': {
        'State of Mexico': (-6, 'Central Standard Time (CST)'),
        'Baja California': (-8, 'Pacific Standard Time (PST)')
},
'Micronesia': {
        'Pohnpei': (11, 'Pohnpei Time (PONT)'),
        'Yap': (10, 'Yap Time (YAPT)')
},
'Mongolia': {
        'Ulaanbaatar': (8, 'Ulaanbaatar Time (ULAT)'),
        'Hovd': (7, 'Hovd Time (HOVT)'),
},
'New Zealand': {
        'New Zealand': (13, 'New Zealand Standard Time (NZST)'),
        'Chatham Islands': (13.75, 'Chatham Standard Time (CHAST)')
},
'Papua New Guinea': {
        'Papua New Guinea': (10, 'Papua New Guinea Time (PGT)'),
        'Bougainville': (11, 'Bougainville Standard Time (BST)')
},
'Russia': {
        'Kaliningrad': (2, 'Kaliningrad Time (KALT)'),
        'Moscow': (3, 'Moscow Time (MSK)'),
        'Samara': (4, 'Samara Time (SAMT)'),
        'Yekaterinburg': (5, 'Yekaterinburg Time (YEKT)'),
        'Omsk': (6, 'Omsk Time (OMST)'),
        'Krasnoyarsk': (7, 'Krasnoyarsk Time (KRAT)'),
        'Irkutsk': (8, 'Irkutsk Time (IRKT)'),
        'Yakutsk' : (9, 'Yakutsk Time (YAKT)'),
        'Vladivostok': (10, 'Vladivostok Time (VLAT)'),
        'Magadan': (11, 'Magadan Time (MAGT)'),
        'Kamchatka': (12, 'Kamchatka Time (PETT)'),
},
'United States': {
        'New York': (-5, 'Eastern Standard Time (EST)'),
        'Alabama': (-6, 'Central Standard Time (CST)'),
        'Colorado': (-7, 'Mountain Standard Time (MST)'),
        'California': (-8, 'Pacific Standard Time (PST)'),
        'Alaska': (-9, 'Alaska Standard Time (AKST)'),
        'Hawaii': (-10, 'Hawaii-Aleutian Standard Time (HST)')
}
}



# initialising offset_hours and display_frame              
offset_hours = 0
display_frame = ctk.CTkFrame(app)

# button function                    
def check_time_button():
 global single_timezone_country_time_display
 global offset_hours
 global display_frame
 display_frame.grid_forget()
 if countries_optionmenu.get() in ["Australia", "Brazil", "Canada", 'Democratic Republic of the Congo', "Indonesia", "Kazakhstan", "Kiribati", "Mexico",
        "Micronesia", "Mongolia", "New Zealand", "Papua New Guinea", "Russia", "United States"]:
        display_frame = ctk.CTkFrame(app, fg_color="#828385")
        display_frame.grid(column = 1, row = 5, sticky = "news", rowspan = 4, columnspan = 3)
        info_frame = ctk.CTkFrame(display_frame, fg_color = "#828385")
        info_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
        for country, timezone_info in multiple_timezone_countries_info.items():
         if countries_optionmenu.get() == country: 
                time_in_country_label = ctk.CTkLabel(app, font=("Consolas", 25), text = "Time in " + country + ":", text_color="white")
                time_in_country_label.grid(column = 1, row = 4, columnspan = 3)

                country_dashed = country.replace(" ", "-").lower()
                country_flag = ctk.CTkImage(dark_image=Image.open(f"images/{country_dashed}.png"), size=(200, 200))
      
                country_flag_label = ctk.CTkLabel(app, image=country_flag, text="")
                country_flag_label.grid(column=4, row=4, sticky="news")

                
                for timezone_state, (offset_hours, timezone) in timezone_info.items():
                                 utc = datetime.now()
                                 timezone_time = utc + timedelta(hours = offset_hours)

                                 display_text = f"{timezone_state},  {timezone}  -  {timezone_time.strftime('%Y-%m-%d %H:%M:%S')}"
                                   
                                 timezone_display = ctk.CTkLabel(info_frame, text = display_text, font=("Consolas", 20), pady = 5, text_color="black")
                                 timezone_display.pack() 
                                           
 else:
    for country, single_timezone_country_time_info in single_timezone_countries_info.items():
        if countries_optionmenu.get() == country:
            
                 utc = datetime.utcnow()
                 offset_hours = single_timezone_country_time_info[0]
                 timezone = single_timezone_country_time_info[1]
                 country_time = utc + timedelta(hours = offset_hours)

                 time_in_country_label = ctk.CTkLabel(app, font=("Consolas", 25), text = "Time in " + country + ":", text_color="white")
                 time_in_country_label.grid(column = 1, row = 4, columnspan = 3)
                 country_dashed = country.replace(" ", "-").lower()
                 country_flag = ctk.CTkImage(dark_image=Image.open(f"images/{country_dashed}.png"), size = (200, 200))

                 country_flag_label = ctk.CTkLabel(app, image = country_flag, text = "")
                 country_flag_label.grid(column = 4, row = 4, sticky = "nsew")

                 display_frame = ctk.CTkFrame(app, fg_color="#828385")
                 display_frame.grid(column = 2, row = 5, sticky = "news", rowspan = 2)

                 info_text = f"{country} \n {timezone}"
                 info_display = ctk.CTkLabel(display_frame, font=("Consolas", 20), text = info_text, text_color="black")
                 info_display.pack(pady = 50)
                 single_timezone_country_time_display = ctk.CTkLabel(display_frame, font=("Consolas", 20), text =  country_time.strftime('%Y-%m-%d %H:%M:%S'), text_color="black")
                 single_timezone_country_time_display.pack(pady = 20)

                 # function to update time continuously
                 def single_timezone_country_live():
                    global offset_hours 
                    utc = datetime.utcnow()
                    country_time = utc + timedelta(hours = offset_hours)
                    single_timezone_country_time_display.configure(text = country_time.strftime('%Y-%m-%d %H:%M:%S'))
                    app.after(1000, single_timezone_country_live)           
                 single_timezone_country_live()

# button to run program
time_button = ctk.CTkButton(app,font=("Consolas", 20), text = "Check Time", width = 200, height=50, command = check_time_button, fg_color="#1d6b8f")
time_button.grid(column = 2, row = 3)


app.mainloop()