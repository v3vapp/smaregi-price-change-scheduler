### This app remotely controls the smaregi website and set new prices and application dates.  

As Smaregi (POS register service) does not offer a method for scheduling price changes through their API, this application utilizes manipulation of their website and configuration to achieve this purpose.
  
## Note for activation
1, create .env file for sumaregi user name and password.  
SMAREGI_EMAIL=foo@gmail.com   
SMAREGI_PASSWORD=abcd1234   
   
2, Currently, this application depends on chromedriver-binary.  
It requires the exact same version as your GoogleChrome.
