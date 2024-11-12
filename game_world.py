world = [[] for _ in range(4)]

collision_pairs={}
def add_collision_pair(group,a,b):
    if group not in collision_pairs:
        print(f'NEW group {group} added......')
        collision_pairs[group]=[ [] , [] ]
    if a:
        print(f'group {group} : {a} added......')
        collision_pairs[group][0].append(a)
    if b:
        print(f'group {group} : {b} added......')
        collision_pairs[group][1].append(b)



def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

def add_object(o, depth = 0):
    world[depth].append(o)

def add_objects(ol, depth = 0):
    world[depth] += ol


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o  #메모리 삭제
            return
    raise ValueError('Cannot delete non existing object')

def clear():
    for layer in world:
        layer.clear()



# fill here
def collide(a, b):

    al,ab,ar,at=a.get_bb()
    bl,bb,br,bt= b.get_bb()


    if ar<bl: return False
    if al>br: return False
    if at<bb: return False
    if ab>bt : return False

    return True # 충돌발생



def handle_collisions():
    for group,pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a,b):
                    print(f'{group} collide')
                    a.handle_collision(group,b)
                    b.handle_collision(group,a)
    return None
