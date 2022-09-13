from collections import deque


class Gun:
    def __init__(self, bullets, barrel_size):
        self.barrel_size = barrel_size
        self.barrel = deque()
        self.bullets_stack = bullets
        self.reload()

    def shoot(self):
        if len(self.barrel) > 1:
            return [self.barrel.popleft()]
        else:
            if self.barrel:
                if not self.reload():
                    return self.barrel.popleft(), 'Reloading!'
                return [self.barrel.popleft()]

    def reload(self):
        if not self.bullets_stack:
            return 1
        i = 0
        while i < self.barrel_size and self.bullets_stack:
            i += 1
            self.barrel.append(self.bullets_stack.pop())

    def left_bullets(self):
        return len(self.barrel) + len(self.bullets_stack)


bullet_cost = int(input())
barrel_size = int(input())
ammunition = list(map(int, input().split()))

gun = Gun(ammunition, barrel_size)

locks = deque(list(map(int, input().split())))

prize = int(input())
shooting_sanction = 0

while locks:
    shoot_ret = gun.shoot()
    if shoot_ret:
        bullet, *reload = shoot_ret
        shooting_sanction += bullet_cost
        if locks[0] >= int(bullet):
            locks.popleft()
            print('Bang!')
        else:
            print('Ping!')

        if reload:
            print(reload.pop())

    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
else:
    print(f"{gun.left_bullets()} bullets left. Earned ${prize - shooting_sanction}")
