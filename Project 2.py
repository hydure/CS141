# Colin Fox Lightfoot
# CFLightfoot@email.wm.edu
# (540)-538-2538
#
# This program runs an expert system for diagnosing a fever, and possibly other,
# symptoms by proposing possibilities once a series of queries are answer using
# a 'Y' or 'y' for a 'yes' response and any other character, perferably 'n'.
# The queries are done in a manner that uses the responses from previous
# queries to determine future queries. The first query asks, "Do you have a 
# fever (y/n)", and if the response is anything other than a case of 'Y', then
# the program announces no recommendation can be made. If the initial query
# indicates that a user does have a fever, then a follow-up query is asked.
# Based on the response to that query, other queries are made until possible
# recommendations are reached. An echo-print of each response to each query is 
# printed after each response is inputted. After completing a diagnosis, the
# user is asked if he/she wants to run the program again. The response is then
# echo-printed; if the response is a case of "Y", then the program is run again,
# if the answer is anything else, the program is terminated.

import sys

# Sets up the initial setup of the program and then asks if the user has a
# fever.
print("\nFever Diagnostic Tool")
print("---------------------\n\n\
Please note that this program performs no true diagnostic\nactivity.",end = " ")
print("No decisions should be made based upon the tool's\nanalysis.", end = " ")
print("If users have a fever, they should contact their\ndoctor.")

print()
diagnosisAnswer = input("Do you have a fever (y,n): ")
ignoreCase4DiagnosisAnswer = diagnosisAnswer.lower()
print(diagnosisAnswer)

# If the user does not have a fever.
while ignoreCase4DiagnosisAnswer != 'y':
    
    print("\nSymptoms\n* None\n\nDiagnosis\n    \
    Insufficient information to list possibilities.\n\n")
    diagnosisAnswer = input("Would you like to input another set of symptoms? ")
    ignoreCase4DiagnosisAnswer = diagnosisAnswer.lower()
    print(diagnosisAnswer)

    # If the user is running the program again, inputs 'y' to having a fever.
    if ignoreCase4DiagnosisAnswer == 'y':
        print("\nFever Diagnostic Tool")
        print("---------------------\n")
        print("Please note that this program performs no true", end=" ")
        print("diagnostic\nactivity. No decisions should be made", end=" ")
        print("based upon the tool's\nanalysis. If users have a", end=" ")
        print("fever, they should contact their\ndoctor.")        
        print()
        diagnosisAnswer = input("Do you have a fever (y,n): ")
        ignoreCase4DiagnosisAnswer = diagnosisAnswer.lower()
        print(diagnosisAnswer)        

    # Exits the program.    
    else:
        sys.exit()    


# If the user answered yes to having a fever. Having a fever is included with
# every reason for a possibility, even though it isn't listed as one in the
# following comment lines.
while ignoreCase4DiagnosisAnswer == 'y':    
    
    # If the user says yes to coughing.
    if ignoreCase4DiagnosisAnswer == 'y':
        answer = input("Are you coughing (y,n): ")
        ignoreCase = answer.lower()
        print(answer)        

        # If the user is short of breath, wheezing, or coughing up phlegm.
        if ignoreCase == 'y':
            answer = ("Are you short of breath or wheezing or " \
                      "coughing up phlegm (y,n): ")
            answer = input(answer)
            ignoreCase = answer.lower()
            print(answer)        

            # Explains the possibilities for coughing and wheezing.
            if ignoreCase == 'y':
                print("\nSymptoms\n* Fever\n* Coughing\n*", end= " ")
                print("Short of breath or wheezing or coughing", end=" ")
                print("up phlegm\n\nDiagnosis\n       ", end= " ")
                print("Possibilities include pneumonia or infection", end= " ")
                print("of airways.\n\n")
                
            # If the user answered no to the wheezing question.
            else:
                answer = input("Do you have a headache (y,n): ")
                ignoreCase = answer.lower()
                print(answer)

                # Explains the possibilities for coughing and having a headache.
                if ignoreCase == 'y':
                    print("\nSymptoms\n* Fever\n* Coughing\n* Headache\n\n"\
                          "Diagnosis\n        Possibilities include viral "\
                          "infection.\n\n")
                    
                # If the user answer no to the headache question.
                else:
                    answer = input("Do you have a sore throat (y,n): ")
                    ignoreCase = answer.lower()
                    print(answer)

                    # Explains the possibilities for coughing and a sore throat.
                    if ignoreCase == 'y':
                        print("\nSymptoms\n* Fever\n* Coughing\n* Sore Throat" \
                              "\n\nDiagnosis\n        Possibilities include "\
                              "throat infection.\n\n")
                        
                    # If the user sats no to a sore throat.
                    else:
                        answer = input("Do you have back pain just above the "\
                                       "waist with chills and fever (y,n): ")
                        ignoreCase = answer.lower()
                        print(answer)

                        # Explains the possibilities for coughing and back pain.
                        if ignoreCase == 'y':
                            print("\nSymptoms\n* Fever\n* Coughing\n* Back "\
                                  "Pain just above the waist with chills and "\
                                  "fever\n\nDiagnosis\n        Possibilities"\
                                  " include kidney infection.\n\n")
                            
                        # If the user says no to having back pain
                        else:
                            answer = input("Do you have pain urinating or are "\
                                           "urinating more often (y,n): ")
                            ignoreCase = answer.lower()
                            print(answer)

                # Explains the possibilities of coughing and painful urination.
                            if ignoreCase == 'y':
                                print("\nSymptoms\n* Fever\n* Coughing\n* "\
                                      "Pain urinating or urinating more often"\
                                      "\n\nDiagnosis\n        Possibilities "\
                                      "include urinary tract infection.\n\n")
                                
                            # Explains that not enough information was provided.
                            else:
                                print("\nSymptoms\n* Fever\n* Coughing\n\n"\
                                      "Diagnosis\n    Insufficient "\
                                      "information to list possibilities.\n\n")
                                
        # If the user responded no to coughing.        
        else:
            answer = input("Do you have a headache (y,n): ")
            ignoreCase = answer.lower()
            print(answer)

            # If the user has a headache.
            if ignoreCase == 'y':
                answer = input("Are you experiencing any of the following:\n "\
                               "pain when bending your head forward, nausea "\
                               "or vomiting,\n bright light hurting your eyes"\
                               ", drowsiness, or confusion (y,n): ")
                ignoreCase = answer.lower()
                print(answer)

                # If the user has a headache and said yes to the above question
                # regarding pain with bending forward, etc., listing possible
                # reasons the user may have these symptoms.
                if ignoreCase == 'y':
                    print("\nSymptoms\n* Fever\n* Headache\n* Pain when "\
                          "bending head forward, nausea or vomiting,\n"\
                          "bright light hurting eyes, drowisness, or "\
                          "confusion.\n\nDiagnosis\n Possibilities "\
                          "include meningitis\n\n")
                    
                # If the user said yes to headaches, but no to pain when bending
                # forward. 
                else:
                    answer = input("Are you vomiting or have had diarrhea "\
                                   "(y,n): ")
                    ignoreCase = answer.lower()
                    print(answer)

                    # Explains the possibilities for why the user has a headache
                    # and is vomitting or has had diarrhea.
                    if ignoreCase == 'y':
                        print("\nSymptoms\n* Fever\n* Headache\n* Vomiting or "\
                              "diarrhea\n\nDiagnosis\n Possibilities "\
                              "include digestive tract infection.\n\n")
                        
                    # Explains that not enough information was provided.
                    else:
                        print("\nSymptoms\n* Fever\n\nDiagnosis\n        "\
                              "Insufficient information to list "\
                              "possibilities.\n\n")
                        
            # If the user responded no to having a headache.            
            else:
                answer = input("Are you vomiting or have had diarrhea (y,n): ")
                ignoreCase = answer.lower()
                print(answer)

                # Explains the possibilities for why the user is vomitting or
                # has had diarrhea.
                if ignoreCase == 'y':
                    print("\nSymptoms\n* Fever\n* Vomiting or "\
                          "diarrhea\n\nDiagnosis\n Possibilities "\
                          "include digestive tract infection.\n\n")
                    
                # Explains that not enough information was provided.
                else:
                    print("\nSymptoms\n*Fever\n\nDiagnosis\n"\
                          "        Insufficient information to list "\
                          "possibilities.\n\n")
                    
    # If the user said no to having a fever for the following query series.
    else:       
        print("\nSymptoms\n*Fever\n\nDiagnosis\n"\
            "        Insufficient information to list possibilities.\n\n")

    # Allows for the user to input another set of symptoms to be run through
    # the program.
    diagnosisAnswer = input("Would you like to input another "\
                            "set of symptoms? ")
    ignoreCase4DiagnosisAnswer = diagnosisAnswer.lower()
    print(diagnosisAnswer)
            
    # Runs the program again.
    if ignoreCase4DiagnosisAnswer == 'y':
        print("\nFever Diagnostic Tool")
        print("---------------------\n")
        print("Please note that this program performs no true", end=" ")
        print("diagnostic\nactivity. No decisions should be made", end=" ")
        print("based upon the tool's\nanalysis. If users have a", end=" ")
        print("fever, they should contact their\ndoctor.")        
        print()
        diagnosisAnswer = input("Do you have a fever (y,n): ")
        ignoreCase4DiagnosisAnswer = diagnosisAnswer.lower()
        print(diagnosisAnswer)                    
                            
    # Exits the program.                
    else:
        sys.exit()
    
    # If the user does not have a fever.    
    while ignoreCase4DiagnosisAnswer != 'y':
            
        print("\nSymptoms\n* None\n\nDiagnosis\n        "\
              "Insufficient information to list possibilities.\n\n")
        diagnosisAnswer = input("Would you like to input another set of "\
                                "symptoms? ")
        ignoreCase4DiagnosisAnswer = diagnosisAnswer.lower()
        print(diagnosisAnswer)
        
        # If the user is running the program again, inputs 'y' to having a
        # fever.
        if ignoreCase4DiagnosisAnswer == 'y':
            print("\nFever Diagnostic Tool")
            print("---------------------\n")
            print("Please note that this program performs no true", end=" ")
            print("diagnostic\nactivity. No decisions should be made", end=" ")
            print("based upon the tool's\nanalysis. If users have a", end=" ")
            print("fever, they should contact their\ndoctor.")        
            print()
            diagnosisAnswer = input("Do you have a fever (y,n): ")
            ignoreCase4DiagnosisAnswer = diagnosisAnswer.lower()
            print(diagnosisAnswer)        
        
        # Exits the program.    
        else:
            sys.exit()