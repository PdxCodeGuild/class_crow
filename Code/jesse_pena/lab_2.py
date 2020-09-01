# madlib reference https://www.it.iitb.ac.in/~vijaya/ssrvm/worksheetscd/getWorksheets.com/Language%20Arts/madlibsdoc.pdf

def madlib():
    adjective_1 = input('Type an adjective: ')
    adjective_2 = input('Type an adjective: ')
    plural_noun = input('Type a plural noun: ')
    noun = input('Type a noun: ')
    adverb_1 = input('Type an adverb: ')
    number = input('Type a number: ')
    past_tense_verb_1 = input('Type a past tense verb: ')
    est_adjective = input('Type an advective that ends in -est: ')
    past_tense_verb_2 = input('Type a past tense verb: ')
    adverb_2 = input('Type an adverb: ')
    adjective_2 = input('Type an adjective')
    


    example_madlib = f'Today, my fabulous camp group went to a (an) {adjective_1} amusement park. It was a fun park with lots of cool {plural_noun} and enjoyable play structures. When we got there, my kind counselor shouted loudly, "Everybody off the {noun}." We all pushed out in a terrible hurry. My counselor handed out yellow tickets, and we scurried in. I was so excited! I couldn\'t figure out what exciting thing to do first. I saw a scary roller coaster I really liked so, I {adverb_1} ran over to get in the long line that had about {number} people in it. When I finally got on the roller coaster I was {past_tense_verb_1}. In fact I was so nervous my two knees were knocking together. This was the {est_adjective} ride I had ever been on! In about two minutes I heard the crank and grinding of the gears. That\'s when the ride began! When I got to the bottom, I was a little {past_tense_verb_2} but I was proud of myself. The rest of the day went {adverb_2}. It was a(n) {adjective_2} day at the fun park.'
    print(example_madlib)



if __name__ == "__main__":
    madlib()