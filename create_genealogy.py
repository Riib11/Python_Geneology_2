import genealogy, genealogy_multitraits, csv_creator, dot_creator

###################
### MULTI TRAIT ###
###################

generations = 4
generation_sizes = 4

a = 0
p = 0
t = 1
parents = 2
traits = [1.2]

def multitrait(dot,csv):
    genealogy_multitraits.init_genealogy()
    gen_data = genealogy_multitraits.make_genealogy( name="MULTITRAIT_example1", generations=generations, generation_sizes_function=lambda x: generation_sizes ,parents=parents, trait_factor=t, popular_factor=p, age_factor=a, traits=traits)
    if dot:
        dot_creator.create_dot(gen_data,False,True)
    if csv:
        csv_creator.create_csv(gen_data)

multitrait(True,False)


####################
### SINGLE TRAIT ###
####################

a = 1
p = 1
t = 1
parents = 4
trait_weights = [2,1]

def singletrait(dot,csv):
    genealogy.init_genealogy()
    gen_data = genealogy.make_genealogy( name="SINGLETRAIT", generations=100, generation_sizes_function=lambda x: 50, parents=parents, balanced=True, trait_factor=t, age_factor=a, popular_factor=p, trait_weights=trait_weights )
    if dot:
        dot_creator.create_dot(gen_data)
    if csv:
        csv_creator.create_csv(gen_data)

# singletrait(True,False)