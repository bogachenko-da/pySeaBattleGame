# Игра "Морской бой"

## Описание игры


- Интерфейс приложения представляет собой консольное окно с двумя полями 6х6.

- Игрок играет с компьютером. Компьютер делает ходы наугад, но не ходит по тем клеткам, в которые он уже сходил.

- Корабли размещаются случайным образом на расстоянии минимум одна клетка друг от друга.

- На каждой доске (у компьютера и у игрока) находится следующее количество кораблей: 1 корабль на 3 клетки, 2 корабля на 2 клетки, 4 корабля на одну клетку.

- Игроку запрещено стрелять в одну и ту же клетку несколько раз. При ошибках хода игрока возникает исключение.

- Буквой X помечаются подбитые корабли, буквой T — промахи, символом "." - контур уничтоженного корабля.

- Побеждает тот, кто быстрее всех разгромит корабли противника.