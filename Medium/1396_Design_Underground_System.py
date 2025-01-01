class UndergroundSystem:
    def __init__(self):
        self.check_in_data = {}
        self.travel_times = {}

    def checkIn(self, id: int, stationName: str, t: int):
        self.check_in_data[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int):
        start_station, check_in_time = self.check_in_data.pop(id)
        travel_time = t - check_in_time
        
        if (start_station, stationName) not in self.travel_times:
            self.travel_times[(start_station, stationName)] = (0, 0)
        total_time, count = self.travel_times[(start_station, stationName)]
        self.travel_times[(start_station, stationName)] = (total_time + travel_time, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_times[(startStation, endStation)]
        return total_time / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)