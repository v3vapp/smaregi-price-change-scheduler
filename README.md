### This app remotely controls the smaregi website and set new prices and application dates.  

As Smaregi (POS register service) does not offer a method for scheduling price changes through their API, this application manipulate their website and achieve this purpose.
  
### Note for activation
1, create .env file for sumaregi username and password like below.  
SMAREGI_EMAIL=foo@gmail.com   
SMAREGI_PASSWORD=abcd1234   
   
2, Currently, this application depends on chromedriver-binary.  
It requires the exact same version as your GoogleChrome.
