from http import server
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 550)
server.starttls()
server.login('hrishikesh.panigrahi38@gmail.com' , 'time pass')
server.sendmail('hrishikesh.panigrahi38@gmail.com'
                'nandini.sahu.panigrahi@gmail.com'
                'this is a practice mail'
                )