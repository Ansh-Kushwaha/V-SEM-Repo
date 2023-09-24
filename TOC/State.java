import java.util.*;

public class State {
    public List<Character> symbols;
    public HashMap<Character, State> transitions;

    public State(List<Character> symbols) {
        this.symbols = symbols;
        this.transitions = new HashMap<>();
    }
}