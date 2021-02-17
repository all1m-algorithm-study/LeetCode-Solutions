class ParkingSystem {
    public int[] cap = new int[4];
    public int[] now = {0, 0, 0, 0};
    public ParkingSystem(int big, int medium, int small) {
        cap[1] = big;
        cap[2] = medium;
        cap[3] = small;
    }
    
    public boolean addCar(int carType) {
        if(now[carType] < cap[carType]) {
            now[carType]++;
            return true;
        }
        return false;
    }
}
