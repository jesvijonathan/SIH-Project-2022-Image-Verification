!run main.py to start and test the logic...!

for now, i have done the backend and main logic

whats remaining is,
creating a flask hosting application
creating a web/admission portal similar to government one
linkinh the application
checking and testing trials, and record accuracy
find beter solution
optimize
and other crap, we will see ...

So what will the final design look like ?

Basically, we make a website similar to government admission portals & have the user fill in details,
but when the user uploads a passport size photo & their signature, we verify whether it has been uploaded under the correct place holders (signature under upload your signaure plcaeholder & photo under upload your passport size photo placeholder),
so once the user hits submit or after uploading the photo, we have a method that firtsly check if the photo has a face in it & the signature photo has a sign in it, if this case passes then we ignore and continue, but if the photos are wrong and does not have a face or sign, then we notify the user, i thought of another case where, if the signature and passport photo are uploaded, but they are uploaded under the worng placeholder, we could give them a prompt and swap it automatically from our side.. (thats exactly why i have added a config file in this project, just so that we can enable/disable experimental features and display them if required)
and in the end presentation is important for our project,
so i thought of hosting it for a week before presentation of our project,
the user, does not have to see the back end, we just have to send them the website/demo link and let them use it (or) we make a pre recorded video of our project which would be great..

the back end is O.K as of now, i want bharath & arun to replicate the government portal (css & html stuff only) meanwhile i have to create a flask application to get data & return/process the result

lets get to work,

TRY TO COMPLETE AS SOON AS POSSIBLE !
