import wikipedia

main_page = wikipedia.WikipediaPage('Online chat')
see_also= main_page.section("See also")


list_of_new_lines = [-1]
see_alsos_deep=[]
checked_yet=[]


def countSeeMores():
    for pos,char in enumerate(see_also):
        if(char == '\n'):
            list_of_new_lines.append(pos)



def seeAlsosDeep(list_of_new_lines):
    for x in range(len(list_of_new_lines)-1):
        see_alsos_deep.append(see_also[list_of_new_lines[x]+1:list_of_new_lines[x+1]])
    see_alsos_deep.append(see_also[list_of_new_lines[x+1]+1:])

    for x in see_alsos_deep:
        checked_yet.append(x)
        print("see alsos dla :"+x)
        see_also_main_page=wikipedia.WikipediaPage(x)
        test=see_also_main_page.section("See also")
        checked_yet.append(test)
        print(checked_yet)
        print(len(checked_yet))


countSeeMores()
seeAlsosDeep(list_of_new_lines)