# -*- coding: utf-8 -*-

my_name = "Yuan Zihong"
my_age = 99 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
gender = '男'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "he's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hait." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print "他的性别是%s." % gender
print "He is %r" % gender

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight) 