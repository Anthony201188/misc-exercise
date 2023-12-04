# CSV data types

## Task 1

###  - Split the string into a list of strings
###  - One line of data is one item in the list
###  - Save the list of strings in a variable called `lines`
###  - Print the amount of lines
###  - Loop over the lines using a `for` loop and print every 5th line


print("********************")
print("TASK 1 ")
print()
print()
print("list of data")
print()
data = """id,first_name,last_name,email,ip_address
1,Jennine,Kohnert,jkohnert0@disqus.com,45.55.73.106
2,Katalin,Nolda,knolda1@123-reg.co.uk,223.30.112.215
3,Atalanta,Kaming,akaming2@gmpg.org,254.219.7.208
4,Kassie,Covell,kcovell3@cafepress.com,150.145.187.71
5,Vonni,Dignam,vdignam4@cafepress.com,138.219.98.53
6,Billie,Neubigging,bneubigging5@addthis.org,180.79.192.175
7,Etan,Peers,epeers6@cafepress.com,199.1.3.70
8,Pail,Walcher,pwalcher7@cafepress.com,199.170.155.126
9,Edlin,Kosel,ekosel8@columbia.edu,217.59.107.252
10,Jennifer,Tibalt,jtibalt9@sun.com,73.29.190.227
11,Douglas,Howe,dhowea@cafepress.com,93.94.19.71
12,Galina,Antoniewski,gantoniewskib@freewebs.com,69.177.160.104
13,Emelita,Pauer,epauerc@house.gov,178.243.169.131
14,Edmon,Cleugh,POTATOKING.2000@furl.net,100.219.252.98
15,kyo,zipulimakkarakeitto,kz@guardian.com,78.226.120.240
16,Harlin,Goodrich,hgoodrichf@guardian.com,232.242.92.122
17,Paddie,Brittain,pbrittaing@jigsy.com,230.116.80.29
18,Blisse,Barbrook,bbarbrookh@nytimes.com,153.237.126.205
19,Latia,Roughey,lrougheyi@guardian.co.uk,184.128.166.8
20,Gregoire,Castelow,gcastelowj@51.la,87.181.120.134
21,lorenza,kurn,ljurnk@nsw.gov.au,192.238.146.135
22,Dulciana,Wilce,dwilcel@noaa.gov,234.245.232.7
23,Boyd,Sponton,bspontonm@guardian.com,106.75.217.74
24,Lenora,Issard,lissardn@guardian.com,167.91.15.190
25,Lissi,Davidovitz,ldavidovitzo@guardian.com,48.7.220.5"""

# First will initiate the variable lines and split the data into lines using the split methof it the \n or new line character
lines = data.split(("\n"))
print()


#Then print the new variable
print( lines)

#print the number of the lines using the length method.
print("number of lines equals: ",len(lines))
print()



# Here I have looped over the lines variable and used the range and length method to return an the intiger number of each indexed line (0-26)
#I then saved that intiger as variable "i", I then used a condtional if statment and added one to account for the index starting a zero
#finially I used the modulus function to see if the intigers stored in "i" where divisible by 5 with no remainder
#finally printing those lines by using the "i" varibale as the index number from the list in a print statemnt
for i in range(len(lines)):
    if (i + 1) % 5 == 0:
        print("every 5th line is as follows")
        print("...")
        print(lines[i])
print()
print()
print("END OF TASK 1")
print("*********************")

## Task 2

###    - Loop over the lines again
###    - Skip the first line (called the header line)
###    - Split each line by the commas, saving the result to a variable
###    - Using that variable, print only the email addresses of each user

print("********************")
print("TASK 2 ")
print()
print()



#first removing the first line by looping over a range of numbers from 1-(the length of the lines variables(which is the number of lines of data we have))
email_add = ""
for i in range(1, len(lines)):
    split_lines = lines[i].split(",")  # Then I split those lines using the variable i as the index number of each element in the list "lines" and put them on new lines so they are easy to read
    email_add += split_lines[3]
    print(split_lines[3]) # then only print the 4th item from each line.

print()
print()
print("END OF TASK 2")
print("*********************")

print("********************")
print("TASK 3 ")
print()
print()

## Task 3

###- Find out and print how many users have an email address with `.co.uk` in it
###- Find out and print how many users first name OR last name starts with a "K" (uppercase or lowercase)
containing = 0
co_uk = ".co.uk"
print(email_add)
if email_add.find(".co.uk"):
        containing += 1
print(containing)

# ctrl 