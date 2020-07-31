import pandas as pd
import matplotlib.pylab as plt
import missingno as msno
from matplotlib import pyplot as plt

data = pd.read_csv("data.csv")

def industry():

    Administrative_Services =("Archiving Service, Call Center, Collection Agency, College Recruiting, Courier Service, Debt Collections, Delivery, Document Preparation, Extermination Service, Facilities Support Services, Housekeeping Service, Office Administration, Packaging Services, Physical Security, Staffing Agency, Trade Shows, Virtual Workforce").replace(', ', '|' )
    data["Administrative_Services"] = data["Industries"].str.contains(Administrative_Services)

    Advertising = ("Ad Exchange, Ad Network, Ad Retargeting, Ad Server, Ad Targeting, Advertising, Advertising Platforms, Affiliate Marketing, Local Advertising, Mobile Advertising, Outdoor Advertising, SEM, Social Media Advertising, Video Advertising").replace(', ', '|' )
    data["Advertising"] = data["Industries"].str.contains(Advertising)

    Agriculture =("Agriculture, AgTech, Animal Feed, Aquaculture, Equestrian, Farming, Forestry, Horticulture, Hydroponics, Livestock").replace(', ', '|' )
    data["Agriculture"] = data["Industries"].str.contains(Agriculture)

    Apps =("App Discovery, Apps, Consumer Applications, Enterprise Applications, Mobile Apps, Reading Apps, Web Apps").replace(', ', '|' )
    data["Apps"] = data["Industries"].str.contains(Apps)

    Artificial_Intelligence =("Artificial Intelligence, Intelligent Systems, Machine Learning, Natural Language Processing, Predictive Analytics").replace(', ', '|' )
    data["Artificial_Intelligence"] = data["Industries"].str.contains(Artificial_Intelligence)

    Biotechnology =("Bioinformatics, Biometrics, Biopharma, Biotechnology, Genetics, Life Science, Neuroscience, Quantified Self").replace(', ', '|' )
    data["Biotechnology"] = data["Industries"].str.contains(Biotechnology)

    Clothing_Apparel =("Fashion, Laundry and Dry-cleaning, Lingerie, Shoes").replace(', ', '|' )
    data["Clothing_Apparel"] = data["Industries"].str.contains(Clothing_Apparel)

    Commerce_and_Shopping =("Auctions, Classifieds, Collectibles, Consumer Reviews, Coupons, E-Commerce, E-Commerce Platforms, Flash Sale, Gift, Gift Card, Gift Exchange, Gift Registry, Group Buying, Local Shopping, Made to Order, Marketplace, Online Auctions, Point of Sale, Price Comparison, Rental, Retail, Retail Technology, Shopping, Shopping Mall, Social Shopping, Sporting Goods, Vending and Concessions, Virtual Goods, Wholesale").replace(', ', '|' )
    data["Commerce_and_Shopping"] = data["Industries"].str.contains(Commerce_and_Shopping)

    Community_Lifestyle =("Cannabis, Communities, Dating, Humanitarian, Leisure, Lifestyle, Online Forums, Parenting, Pet, Private Social Networking, Professional Networking, Q&A, Religion, Sex Industry, Social Entrepreneurship, Virtual World, Wedding").replace(', ', '|' )
    data["Community_Lifestyle"] = data["Industries"].str.contains(Community_Lifestyle)

    Consumer_Electronics =("Computer, Consumer Electronics, Drones, Electronics, Google Glass, Mobile Devices, Nintendo, Playstation, Roku, Smart Home, Wearables, Windows Phone, Xbox").replace(', ', '|' )
    data["Consumer_Electronics"] = data["Industries"].str.contains(Consumer_Electronics)

    Consumer_Goods =("Beauty, Comics, Consumer Goods, Cosmetics, DIY, Drones, Eyewear, Fast-Moving Consumer Goods, Flowers, Furniture, Green Consumer Goods, Jewelry, Lingerie, Shoes, Tobacco, Toys").replace(', ', '|' )
    data["Consumer_Goods"] = data["Industries"].str.contains(Consumer_Goods)

    Content_Publishing =("Blogging Platforms, Content Delivery Network, Content Discovery, Content Syndication, Creative Agency, DRM, EBooks, Journalism, News, Photo Editing, Photo Sharing, Photography, Printing, Publishing, Video Editing, Video Streaming").replace(', ', '|' )
    data["Content_Publishing"] = data["Industries"].str.contains(Content_Publishing)

    Data_Analytics =("A/B Testing, Analytics, Application Performance Management, Artificial Intelligence, Big Data, Bioinformatics, Biometrics, Business Intelligence, Consumer Research, Data Integration, Data Mining, Data Visualization, Database, Facial Recognition, Geospatial, Image Recognition, Intelligent Systems, Location Based Services, Machine Learning, Market Research, Natural Language Processing, Predictive Analytics, Product Research, Quantified Self, Speech Recognition, Test and Measurement, Text Analytics, Usability Testing").replace(', ', '|' )
    data["Data_Analytics"] = data["Industries"].str.contains(Data_Analytics)

    Design =("CAD, Consumer Research, Data Visualization, Fashion, Graphic Design, Human Computer Interaction, Industrial Design, Interior Design, Market Research, Mechanical Design, Product Design, Product Research, Usability Testing, UX Design, Web Design").replace(', ', '|' )
    data["Design"] = data["Industries"].str.contains(Design)

    Education =("Charter Schools, College Recruiting, Continuing Education, Corporate Training, E-Learning, EdTech, Education, Edutainment, Higher Education, Language Learning, MOOC, Music Education, Personal Development, Primary Education, Secondary Education, Skill Assessment, STEM Education, Textbook, Training, Tutoring, Vocational Education").replace(', ', '|' )
    data["Education"] = data["Industries"].str.contains(Education)

    Energy =("Battery, Biofuel, Biomass Energy, Clean Energy, Electrical Distribution, Energy, Energy Efficiency, Energy Management, Energy Storage, Fossil Fuels, Fuel, Fuel Cell, Oil and Gas, Power Grid, Renewable Energy, Solar, Wind Energy").replace(', ', '|' )
    data["Energy"] = data["Industries"].str.contains(Energy)


    Events =("Concerts, Event Management, Event Promotion, Events, Nightclubs, Nightlife, Reservations, Ticketing, Wedding").replace(', ', '|' )
    data["Events"] = data["Industries"].str.contains(Events)


    Financial_Services =("Accounting, Angel Investment, Asset Management, Auto Insurance, Banking, Bitcoin, Commercial Insurance, Commercial Lending, Consumer Lending, Credit, Credit Bureau, Credit Cards, Crowdfunding, Cryptocurrency, Debit Cards, Debt Collections, Finance, Financial Exchanges, Financial Services, FinTech, Fraud Detection, Funding Platform, Gift Card, Health Insurance, Hedge Funds, Impact Investing, Incubators, Insurance, InsurTech, Leasing, Lending, Life Insurance, Micro Lending, Mobile Payments, Payments, Personal Finance, Prediction Markets, Property Insurance, Real Estate Investment, Stock Exchanges, Trading Platform, Transaction Processing, Venture Capital, Virtual Currency, Wealth Management").replace(', ', '|' )
    data["Financial_Services"] = data["Industries"].str.contains(Financial_Services)


    Food_Beverage =("Bakery, Brewing, Cannabis, Catering, Coffee, Confectionery, Cooking, Craft Beer, Dietary Supplements, Distillery, Farmers Market, Food and Beverage, Food Delivery, Food Processing, Food Trucks, Fruit, Grocery, Nutrition, Organic Food, Recipes, Restaurants, Seafood, Snack Food, Tea, Tobacco, Wine And Spirits, Winery").replace(', ', '|' )
    data["Food_Beverage"] = data["Industries"].str.contains(Food_Beverage)


    Gaming =("Casual Games, Console Games, Contests, Fantasy Sports, Gambling, Gamification, Gaming, MMO Games, Online Games, PC Games, Serious Games, Video Games").replace(', ', '|' )
    data["Gaming"] = data["Industries"].str.contains(Gaming)

    Government_Military =("CivicTech, Government, GovTech, Law Enforcement, Military, National Security, Politics, Public Safety, Social Assistance").replace(', ', '|' )
    data["Government_Military"] = data["Industries"].str.contains(Government_Military)

    Hardware =("3D Technology, Application Specific Integrated Circuit (ASIC), Augmented Reality, Cloud Infrastructure, Communication Hardware, Communications Infrastructure, Computer, Computer Vision, Consumer Electronics, Data Center, Data Center Automation, Data Storage, Drone Management, Drones, DSP, Electronic Design Automation (EDA), Electronics, Embedded Systems, Field-Programmable Gate Array (FPGA), Flash Storage, Google Glass, GPS, GPU, Hardware, Industrial Design, Laser, Lighting, Mechanical Design, Mobile Devices, Network Hardware, NFC, Nintendo, Optical Communication, Playstation, Private Cloud, Retail Technology, RFID, RISC, Robotics, Roku, Satellite Communication, Semiconductor, Sensor, Sex Tech, Telecommunications, Video Conferencing, Virtual Reality, Virtualization, Wearables, Windows Phone, Wireless, Xbox").replace(', ', '|' )
    data["Hardware"] = data["Industries"].str.contains(Hardware)

    Health_care =("Alternative Medicine, Assisted Living, Assistive Technology, Biopharma, Cannabis, Child Care, Clinical Trials, Cosmetic Surgery, Dental, Diabetes, Dietary Supplements, Elder Care, Electronic Health Record (EHR), Emergency Medicine, Employee Benefits, Fertility, First Aid, Funerals, Genetics, Health Care, Health Diagnostics, Home Health Care, Hospital, Medical, Medical Device, mHealth, Nursing and Residential Care, Nutraceutical, Nutrition, Outpatient Care, Personal Health, Pharmaceutical, Psychology, Rehabilitation, Therapeutics, Veterinary, Wellness").replace(', ', '|' )
    data["Health_care"] = data["Industries"].str.contains(Health_care)

    Information_Technology =("Business Information Systems, CivicTech, Cloud Data Services, Cloud Management, Cloud Security, CMS, Contact Management, CRM, Cyber Security, Data Center, Data Center Automation, Data Integration, Data Mining, Data Visualization, Document Management, E-Signature, Email, GovTech, Identity Management, Information and Communications Technology (ICT), Information Services, Information Technology, Intrusion Detection, IT Infrastructure, IT Management, Management Information Systems, Messaging, Military, Network Security, Penetration Testing, Private Cloud, Reputation, Sales Automation, Scheduling, Social CRM, Spam Filtering, Unified Communications, Video Chat, Video Conferencing, Virtualization, VoIP").replace(', ', '|' )
    data["Information_Technology"] = data["Industries"].str.contains(Information_Technology)

    Lending_Investments =("Angel Investment, Banking, Commercial Lending, Consumer Lending, Credit, Credit Cards, Financial Exchanges, Funding Platform, Hedge Funds, Impact Investing, Incubators, Micro Lending, Stock Exchanges, Trading Platform, Venture Capital").replace(', ', '|' )
    data["Lending_Investments"] = data["Industries"].str.contains(Lending_Investments)

    Internet_Services =("Cloud Computing, Cloud Data Services, Cloud Infrastructure, Cloud Management, Cloud Storage, Darknet, Domain Registrar, E-Commerce Platforms, Ediscovery, Email, Internet, Internet of Things, ISP, Location Based Services, Messaging, Music Streaming, Online Forums, Online Portals, Private Cloud, Product Search, Search Engine, SEM, Semantic Search, Semantic Web, SEO, SMS, Social Media, Social Media Management, Social Network, Unified Communications, Vertical Search, Video Chat, Video Conferencing, Visual Search, VoIP, Web Browsers, Web Hosting").replace(', ', '|' )
    data["Internet_Services"] = data["Industries"].str.contains(Internet_Services)

    Manufacturing =("3D Printing, Advanced Materials, Foundries, Industrial Automation, Industrial Engineering, Industrial Manufacturing, Machinery Manufacturing, Manufacturing, Paper Manufacturing, Plastics and Rubber Manufacturing, Textiles, Wood Processing").replace(', ', '|' )
    data["Manufacturing"] = data["Industries"].str.contains(Manufacturing)

    Media_Entertainment =("Advice, Animation, Art, Audio, Audiobooks, Blogging Platforms, Broadcasting, Celebrity, Concerts, Content, Content Creators, Content Discovery, Content Syndication, Creative Agency, Digital Entertainment, Digital Media, DRM, EBooks, Edutainment, Event Management, Event Promotion, Events, Film, Film Distribution, Film Production, Guides, In-Flight Entertainment, Independent Music, Internet Radio, Journalism, Media and Entertainment, Motion Capture, Music, Music Education, Music Label, Music Streaming, Music Venues, Musical Instruments, News, Nightclubs, Nightlife, Performing Arts, Photo Editing, Photo Sharing, Photography, Podcast, Printing, Publishing, Reservations, Social Media, Social News, Theatre, Ticketing, TV, TV Production, Video, Video Editing, Video on Demand, Video Streaming, Virtual World").replace(', ', '|' )
    data["Media_Entertainment"] = data["Industries"].str.contains(Media_Entertainment)

    Messaging_Telecommunications =("Email, Meeting Software, Messaging, SMS, Unified Communications, Video Chat, Video Conferencing, VoIP, Wired Telecommunications").replace(', ', '|' )
    data["Messaging_Telecommunications"] = data["Industries"].str.contains(Messaging_Telecommunications)

    Mobile =("Android, Google Glass, iOS, mHealth, Mobile, Mobile Apps, Mobile Devices, Mobile Payments, Windows Phone, Wireless").replace(', ', '|' )
    data["Mobile"] = data["Industries"].str.contains(Mobile)

    Music_Audio =("Audio, Audiobooks, Independent Music, Internet Radio, Music, Music Education, Music Label, Music Streaming, Musical Instruments, Podcast").replace(', ', '|' )
    data["Music_Audio"] = data["Industries"].str.contains(Music_Audio)

    Natural_Resources =("Biofuel, Biomass Energy, Fossil Fuels, Mineral, Mining, Mining Technology, Natural Resources, Oil and Gas, Precious Metals, Solar, Timber, Water, Wind Energy").replace(', ', '|' )
    data["Natural_Resources"] = data["Industries"].str.contains(Natural_Resources)

    Navigation_Mapping =("Geospatial, GPS, Indoor Positioning, Location Based Services, Mapping Services, Navigation").replace(', ', '|' )
    data["Navigation_Mapping"] = data["Industries"].str.contains(Navigation_Mapping)

    Payments =("Billing, Bitcoin, Credit Cards, Cryptocurrency, Debit Cards, Fraud Detection, Mobile Payments, Payments, Transaction Processing, Virtual Currency").replace(', ', '|' )
    data["Payments"] = data["Industries"].str.contains(Payments)

    Platforms =("Android, Facebook, Google, Google Glass, iOS, Linux, macOS, Nintendo, Operating Systems, Playstation, Roku, Tizen, Twitter, WebOS, Windows, Windows Phone, Xbox").replace(', ', '|' )
    data["Platforms"] = data["Industries"].str.contains(Platforms)

    Privacy_Security =("Cloud Security, Corrections Facilities, Cyber Security, DRM, E-Signature, Fraud Detection, Homeland Security, Identity Management, Intrusion Detection, Law Enforcement, Network Security, Penetration Testing, Physical Security, Privacy, Security").replace(', ', '|' )
    data["Privacy_Security"] = data["Industries"].str.contains(Privacy_Security)

    Professional_Services =("Accounting, Career Planning, Compliance, Employment, Environmental Consulting, Freelance, Intellectual Property, Legal, Legal Tech, Management Consulting, Outsourcing, Professional Networking, Recruiting, Social Recruiting, Translation Service").replace(', ', '|' )
    data["Professional_Services"] = data["Industries"].str.contains(Professional_Services)

    Real_Estate =("Architecture, Building Maintenance, Building Material, Commercial Real Estate, Construction, Coworking, Facility Management, Fast-Moving Consumer Goods, Green Building, Home and Garden, Home Decor, Home Improvement, Home Renovation, Home Services, Interior Design, Janitorial Service, Landscaping, Property Development, Property Management, Real Estate, Real Estate Investment, Rental Property, Self-Storage, Smart Building, Smart Cities, Smart Home, Timeshare, Vacation Rental").replace(', ', '|' )
    data["Real_Estate"] = data["Industries"].str.contains(Real_Estate)

    Sales_Marketing =("Advertising, Affiliate Marketing, App Discovery, App Marketing, Brand Marketing, Cause Marketing, Content Marketing, CRM, Digital Marketing, Digital Signage, Direct Marketing, Direct Sales, Email Marketing, Lead Generation, Lead Management, Local Advertising, Loyalty Programs, Marketing, Marketing Automation, Mobile Advertising, Multi-level Marketing, Outdoor Advertising, Personal Branding, Public Relations, Sales, Sales Automation, SEM, SEO, Social CRM, Social Media Advertising, Social Media Management, Social Media Marketing, Sponsorship, Video Advertising").replace(', ', '|' )
    data["Sales_Marketing"] = data["Industries"].str.contains(Sales_Marketing)

    Science_Engineering =("Advanced Materials, Aerospace, Artificial Intelligence, Bioinformatics, Biometrics, Biopharma, Biotechnology, Chemical, Chemical Engineering, Civil Engineering, Embedded Systems, Environmental Engineering, Human Computer Interaction, Industrial Automation, Industrial Engineering, Intelligent Systems, Laser, Life Science, Marine Technology, Mechanical Engineering, Nanotechnology, Neuroscience, Nuclear, Quantum Computing, Robotics, Semiconductor, Software Engineering, STEM Education").replace(', ', '|' )
    data["Science_Engineering"] = data["Industries"].str.contains(Science_Engineering)

    Software =("3D Technology, Android, App Discovery, Application Performance Management, Apps, Artificial Intelligence, Augmented Reality, Billing, Bitcoin, Browser Extensions, CAD, Cloud Computing, Cloud Management, CMS, Computer Vision, Consumer Applications, Consumer Software, Contact Management, CRM, Cryptocurrency, Data Center Automation, Data Integration, Data Storage, Data Visualization, Database, Developer APIs, Developer Platform, Developer Tools, Document Management, Drone Management, E-Learning, EdTech, Electronic Design Automation (EDA), Embedded Software, Embedded Systems, Enterprise Applications, Enterprise Resource Planning (ERP), Enterprise Software, Facial Recognition, File Sharing, IaaS, Image Recognition, iOS, Linux, Machine Learning, macOS, Marketing Automation, Meeting Software, Mobile Apps, Mobile Payments, MOOC, Natural Language Processing, Open Source, Operating Systems, PaaS, Predictive Analytics, Presentation Software, Presentations, Private Cloud, Productivity Tools, QR Codes, Reading Apps, Retail Technology, Robotics, SaaS, Sales Automation, Scheduling, Sex Tech, Simulation, SNS, Social CRM, Software, Software Engineering, Speech Recognition, Task Management, Text Analytics, Transaction Processing, Video Conferencing, Virtual Assistant, Virtual Currency, Virtual Desktop, Virtual Goods, Virtual Reality, Virtual World, Virtualization, Web Apps, Web Browsers, Web Development").replace(', ', '|' )
    data["Software"] = data["Industries"].str.contains(Software)

    Sports =("American Football, Baseball, Basketball, Boating, Cricket, Cycling, Diving, eSports, Fantasy Sports, Fitness, Golf, Hockey, Hunting, Outdoors, Racing, Recreation, Rugby, Sailing, Skiing, Soccer, Sporting Goods, Sports, Surfing, Swimming, Table Tennis, Tennis, Ultimate Frisbee, Volley Ball").replace(', ', '|' )
    data["Sports"] = data["Industries"].str.contains(Sports)

    Sustainability =("Biofuel, Biomass Energy, Clean Energy, CleanTech, Energy Efficiency, Environmental Engineering, Green Building, Green Consumer Goods, GreenTech, Natural Resources, Organic, Pollution Control, Recycling, Renewable Energy, Solar, Sustainability, Waste Management, Water Purification, Wind Energy").replace(', ', '|' )
    data["Sustainability"] = data["Industries"].str.contains(Sustainability)

    Transportation =("Air Transportation, Automotive, Autonomous Vehicles, Car Sharing, Courier Service, Delivery Service, Electric Vehicle, Ferry Service, Fleet Management, Food Delivery, Freight Service, Last Mile Transportation, Limousine Service, Logistics, Marine Transportation, Parking, Ports and Harbors, Procurement, Public Transportation, Railroad, Recreational Vehicles, Ride Sharing, Same Day Delivery, Shipping, Shipping Broker, Space Travel, Supply Chain Management, Taxi Service, Transportation, Warehousing, Water Transportation").replace(', ', '|' )
    data["Transportation"] = data["Industries"].str.contains(Transportation)

    Travel_Tourism =("Adventure Travel, Amusement Park and Arcade, Business Travel, Casino, Hospitality, Hotel, Museums and Historical Sites, Parks, Resorts, Timeshare, Tour Operator, Tourism, Travel, Travel Accommodations, Travel Agency, Vacation Rental").replace(', ', '|' )
    data["Travel_Tourism"] = data["Industries"].str.contains(Travel_Tourism)

    Video =("Animation, Broadcasting, Film, Film Distribution, Film Production, Motion Capture, TV, TV Production, Video, Video Editing, Video on Demand, Video Streaming").replace(', ', '|' )
    data["Video"] = data["Industries"].str.contains(Video)
    return data