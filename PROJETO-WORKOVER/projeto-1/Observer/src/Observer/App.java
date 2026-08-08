package Observer;

public class App {
    public static void main(String[] args) {

        TemperatureObservable observable = new TemperatureObservable();
        new WatchDisplayObserver(observable);

        observable.setTemperature(25);
        observable.setTemperature(30);
    }
}