import heapq

# https://leetcode.com/problems/seat-reservation-manager/

class SeatManager:

    def __init__(self, n: int):
        self.available_seats = list(range(1, n + 1))

    def reserve(self) -> int:
        return heapq.heappop(self.available_seats)

    def unreserve(self, seat_number: int) -> None:
        heapq.heappush(self.available_seats, seat_number)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
