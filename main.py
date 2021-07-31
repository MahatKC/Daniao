from substitution_cyphers.playfair import play_fair
from substitution_cyphers.caesar import rot_n
from transposition_cyphers.railfence import rail_fence
from product_cyphers.product_pipeline import ProductPipeline

p = ProductPipeline()
p.add_cypher(rot_n, 22)
p.add_cypher(rot_n, 4)
p.add_cypher(rail_fence,1)
p.add_cypher(play_fair, "monarchy")
p.run("hermes")

print(p)
p.remove_cypher(2)
print(p)