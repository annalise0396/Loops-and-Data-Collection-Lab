def check_if_classified():    
    target_words = ["james", "london", "mi6", "classified", "paris", "midnight", "nuclear", "asset"]
    classifier = input("Classifier: ")
    
    seperated_classifier = classifier.split()
    
    for words in seperated_classifier:
        if words in target_words:
            print("[CLASSIFIED]", end=" ")
        else:
            print(words, end=" ")
    
            
check_if_classified()


