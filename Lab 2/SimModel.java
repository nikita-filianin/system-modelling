import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;

public class SimModel {
    public static void main(String[] args) {
        Create c = new Create(3.0, 1);
        c.setName("Creator");
        c.setDistribution("unif");
        c.setDelayDev(50);

        Process p1 = new Process(40, 1);
        p1.setName("Processor 1");
        p1.setMaxqueue(5);
        p1.setDistribution("unif");
        p1.setDelayDev(100);

        Process p2 = new Process(50, 1);
        p2.setName("Processor 2");
        p2.setMaxqueue(5);
        p2.setDistribution("unif");
        p2.setDelayDev(100);

        Process p3 = new Process(70, 1);
        p3.setName("Processor 3");
        p3.setMaxqueue(5);
        p3.setDistribution("unif");
        p3.setDelayDev(100);

        Dispose d = new Dispose();
        d.setName("Dispose");

//      One-by-one
        c.setNextElement(p1);
        p1.setNextElement(p2);
        p2.setNextElement(p3);
        p3.setNextElement(d);

//      Priority queue
        PriorityQueue<QueueElement> queue = new PriorityQueue<>();
        queue.add(new QueueElement(p1, 0));
        queue.add(new QueueElement(p2, -1));
        queue.add(new QueueElement(p3, -2));
        c.setNextElementQueue(queue);
        p1.setNextElement(d);
        p2.setNextElement(d);
        p3.setNextElement(d);

//      Random with odds
        HashMap<Double, Element> C_to_P1_P2_P3 = new HashMap<>();
        C_to_P1_P2_P3.put(0.4, p1);
        C_to_P1_P2_P3.put(0.1, p2);
        C_to_P1_P2_P3.put(0.5, p3);
        c.setNextRandomElementArray(C_to_P1_P2_P3);
        p1.setNextElement(d);
        p2.setNextElement(d);
        p3.setNextElement(d);

        ArrayList<Element> list = new ArrayList<>();
        list.add(c);
        list.add(p1);
        list.add(p2);
        list.add(p3);
        list.add(d);
        new Model(list).simulate(10000.0);
    }
}
