public class State {
    private String name;
    private boolean isInitial;
    private boolean isFinal;
    Map<Character, 
    public State(String name, boolean isInitial, boolean isFinal) {
        this.name = name;
        this.isInitial = isInitial;
        this.isFinal = isFinal;
    }

    public boolean isInitial() {
        return isInitial;
    }

    public boolean isFinal() {
        return isFinal;
    }
}