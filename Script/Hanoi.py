def move_disk(fp,tp):
    print("moving disk from",fp,"to",tp)
def move_tower(heigth,from_pole,to_pole,with_pole):
    if heigth>=1:
        move_tower(heigth-1,from_pole, with_pole, to_pole)
        move_disk(from_pole,to_pole)
        move_tower(heigth-1,with_pole,to_pole,from_pole)
def move_disk(fp,tp):
    print("moving disk from",fp,"to",tp)
move_tower(3,"A","B","C")
        
