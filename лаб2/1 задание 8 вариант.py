def main():
    max_number = int(input("Введите максимальное число: "))
    possible_numbers = set(range(1, max_number + 1))
    
   
    test = True
    
    while test:
        question = input('Введите HELP чтобы прервать ').strip()
        
     
        if question == "HELP":
            running = False  
        else:
            
            numbers = set(map(int, question.split()))
            
            
            if len(numbers) == len(possible_numbers) / 2:
                print("NO")
                possible_numbers -= numbers
            else:
               
                yes_option = possible_numbers & numbers
                no_option = possible_numbers - numbers
                
               
                if len(yes_option) >= len(no_option):
                    print("YES")
                    possible_numbers = yes_option
                else:
                    print("NO")
                    possible_numbers = no_option
    
   
    print(" ".join(map(str, sorted(possible_numbers))))

if __name__ == "__main__":
    main()