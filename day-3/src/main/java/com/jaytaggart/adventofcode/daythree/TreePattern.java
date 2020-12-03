package com.jaytaggart.adventofcode.daythree;

public class TreePattern {
    private final String pattern;

    public TreePattern(String pattern) {
        this.pattern = pattern;
    }

    public String getPattern() {
        return pattern;
    }

    public static TreePattern fromString(String s) {
        return new TreePattern(s);
    }
}
