class ParkingSystem {
public:
    int cap[4], now[4] = {0,};
    ParkingSystem(int big, int medium, int small) {
        cap[1] = big;
        cap[2] = medium;
        cap[3] = small;
    }
    
    bool addCar(int carType) {
        if(now[carType] < cap[carType]) {
            now[carType]++;
            return true;
        }
        return false;
    }
};
