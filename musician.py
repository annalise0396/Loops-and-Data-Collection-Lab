def musician_voting():
    end = False
    votes = {}
    while end == False:
        musician = input("Enter a musician: ").strip().title()
        if musician == "Done":
            end = True
        else:
            end = False
            votes[musician] = votes.get(musician, 0) + 1 
            
    if end == True:
        print(" ")
        print("Votes")
        print("------------")
        for musician, count in votes.items():
            print(f"{musician}: {count}")
musician_voting()
