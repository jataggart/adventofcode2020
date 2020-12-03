package com.jaytaggart.adventofcode.daythree;

import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class DayThreeApplication {
    public static void main(String[] args) throws IOException, URISyntaxException {
        List<TreePattern> input = getInput();

        partOne(input);
    }

    private static void partOne(List<TreePattern> input) {
        int count = 0;
        int x = 1;
        char tree = "#".charAt(0);
        for (TreePattern treePattern : input.subList(1, input.size())) {
            x = x + 3;
            String pattern = treePattern.getPattern();
            while (pattern.length() < x + 3) {
                treePattern.extendPattern();
                pattern = treePattern.getPattern();
            }
            if (Objects.equals(tree, pattern.charAt(x - 1))) {
                count++;
            }
        }

        System.out.println("Part One: " + count);
    }

    private static List<TreePattern> getInput() throws URISyntaxException, IOException {
        URI inputResource = Objects.requireNonNull(DayThreeApplication.class.getClassLoader().getResource("input.txt"))
                                   .toURI();
        File inputFile = new File(inputResource);
        return Files.readAllLines(inputFile.toPath())
                    .stream()
                    .map(TreePattern::fromString)
                    .collect(Collectors.toList());
    }
}
