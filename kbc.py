import random

"""
Program of a famous Kbc game i.e inspired from a show Kaun Banega krorepatii- very popular in india
This a program owned by Yogendra Kumar Mishra...yogiimishra14@gmail.com
"""

# question's bag
questions = ['1. pehle istamal kre fir _____  kre Complete this sentence.',
             '2.According to a legend, the capital city of which of these states\n'
             'is said to have derived its name from one of the younger brothers of Lord Rama?',
             '3. From where does Veeru propose to Basanti in Sholay ?',
             '4.  What do you call Indian ice-cream ?',
             '5. Who was the First Commander in Chief of the Kaurava Army ?',
             # level-2
             '6.  Who invented Bicycle ?',
             '7.  Aishwarya Rai was crowned Miss World in which year ?',
             '8. The largest Buddhist Monastery in India is located at...?',
             '9. Which team did Sachin Tendulkar play for in the Ranji Trophy '
             'when he made his debut in first class cricket ?',
             "10. Which is India's first Colour film?",
             '11. Which is the largest aircraft by weight ever built?',
             '12. After which historical or mythological figure did Sri Lanka name its first satellite?',
             '13. Which of these states has had the most number of its governors become presidents of India?'








             ]

# option's bag
options = [' complain', ' tariff', ' vishwas', ' use ',
           ' Uttranchal ', ' Uttar pradesh', ' Jharkhand', ' Madhya Pradesh',
           ' Top of a roof', ' Top of a ladder', ' Top of a hill', ' Top of a water tank',
           ' Sudji Ka Halava', ' Kulfi', ' Gaajar ka Halava', ' Khir ',
           ' Ashvathama', ' Drona', ' Bheeshma', ' Karna',
           ' Leo H Baekeland', ' Karl Benz', ' Evangelista Torricelli', ' Kirkpatrick Macmillan',
           ' 1992', ' 1993', ' 1994', ' 1995',
           ' Gangktok, Sikkim', ' Dharamshala, Himachal Pradesh', ' Tawang, Arunachal Pradesh',
           ' Sarnath, Uttar Pradesh', ' Karnataka', ' Delhi', ' Mumbai', ' Kerela',
           ' Kisan Kanya', ' Mother India', ' Taj Mahal', ' Alam Ara',
           ' Airbus A380-800', ' Antonov AN-225 Mriya', ' Antonov AN-124 Ruslan', ' Hughes H-4 Hercules',
           ' Kuber', ' Buddha', ' Vibhishana', ' Ravana',
           ' Rajasthan', ' Bihar', ' Andhra pradesh', ' Punjab'





           ]

# lifelines
lifelines = ['1. audience poll', '2. 50:50', '3. Flip the question']
answers = [3, 2, 4, 2, 3, 4, 3, 3, 3, 1, 2, 4, 2]

# Main program
def kbc():
    a, b, c, d = 0, 1, 2, 3
    prize = 0
    f = 0
    q = 0
    status = True

    while status:

        if q > 12:
            print('Congratulations you played very well !! You have won ', str(prize), 'rupees.')
            status = False
            break

        print(' ')
        print('Q' + questions[q])
        print('1' + options[a])
        print('2' + options[b])
        print('3' + options[c])
        print('4' + options[d])

        ask = int(input('Type your option 1,2,3 or 4: or type 14 to use lifeline...Type 0 to quit the game :'))

        if ask == answers[f]:
            # prize
            prize += 1000
            print('your answer is correct !! you have won ', str(prize), 'rupees')
            print("  ")
            a, b, c, d, q = a + 4, b + 4, c + 4, d + 4, q + 1
            f += 1

        elif ask == 14:
            # lifelines
            print('\nyour lifelines are :')
            for i in range(0, len(lifelines)):
                print(' ' + lifelines[i])
            h = input('Choose your lifeline by typing correct no. :')
            # lifeline = audience pole
            if h == '1':
                lifelines.remove('1. audience poll')
                print("you have opted audience poll...")
                print("  ")
                c_option = answers[f]
                print('maximum votes are for option no. ' + str(c_option))

                askchoose = input('type y to go with  audience:')
                if askchoose == 'y':
                    prize += 1000
                    print('your answer is correct !! you have won ', str(prize), 'rupees.')
                    print("  ")
                    a, b, c, d, q = a + 4, b + 4, c + 4, d + 4, q + 1
                    f = f + 1
                else:
                    print('Incorrect input !!')
                    # lifeline - (50 : 50)

            elif h == '2':
                print('  ')
                lifelines.remove('2. 50:50')

                print('you have opted the 50-50 lifeline \n so 2 wrongs options will be removed...')

                c_option = answers[f]
                temp_option = [options[a], options[b], options[c], options[d]]

                if c_option < 3:
                    del temp_option[c_option]

                    del temp_option[c_option]
                else:
                    del temp_option[c_option - 2]
                    del temp_option[c_option - 3]
                print('your  question with new options is :')
                print(" ")
                print('Q' + questions[q])
                print('1' + temp_option[0])
                print('2' + temp_option[1])

                ask_second = int(input('Type 1,2 for your answer:'))

                if c_option == 1:
                    check = 1
                elif c_option == 3:
                    check = 1
                else:
                    check = 2

                if ask_second == check:
                    prize += 1000
                    print('your answer is correct !! you have won ', str(prize), 'rupees.')
                    a, b, c, d, q = a + 4, b + 4, c + 4, d + 4, q + 1
                    f += 1
                else:
                    print('oh your answer was wrong !! You have won', str(prize), 'rupees.')
                    print('Thanks for playing !!')
                    status = False
                    # lifeline - Flip the Question
            elif h == '3':
                lifelines.remove('3. Flip the question')
                current_ques = questions[q]
                first_num = current_ques[0]
                print('you have opted flip the question so your question will be changed...\n')
                flip_ques = 'Q' + str(first_num) + ' Which of these places is not located in Mumbai?'
                flip_option = ['The Gateway of India', 'The Kamala Nehru Park', 'The Juhu Beach',
                               'The Charminar'
                               ]
                print(flip_ques)
                print('1 ' + flip_option[0])
                print('2 ' + flip_option[1])
                print('3 ' + flip_option[2])
                print('4 ' + flip_option[3])
                flip_ans = int(input('Type your option 1,2,3 or 4:'))
                if flip_ans == 4:
                    prize += 1000
                    print('your answer is correct !! you have won ', str(prize), 'rupees.')
                    a, b, c, d, q = a + 4, b + 4, c + 4, d + 4, q + 1
                    f += 1
                else:
                    print('oh your answer was wrong !! You have won', str(prize), 'rupees.')
                    print('Thanks for playing !!')
                    status = False
        elif ask == 0:
            print('so your game ends here !!You have won ', str(prize), 'rupees.')
            print('Thanks for playing !!')
            status = False


        else:
            print('oh your answer was wrong !! You have won', str(prize), 'rupees')
            print('Thanks for playing !!')
            status = False


kbc()
