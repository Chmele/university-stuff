package com.company;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.mockito.Mockito;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.HashSet;

import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;

public class SolutionTest {

    private FileSystemDataService s;
    private Solution sol;


    @Before
    public void setUp() throws IOException {
        this.sol = new Solution();
        this.s = Mockito.mock(FileSystemDataService.class);
        sol.setService(s);
        Mockito.when(s.getData("path1")).thenReturn("test word");
        Mockito.when(s.getData("path2")).thenReturn("test words");
        Mockito.when(s.getData("incorrect_path")).thenThrow(new FileNotFoundException());
    }

    @Test
    public void testSolution() throws IOException {
        var t = new HashSet<String>();
        t.add("test");
        t.add("word");

        Assert.assertEquals(sol.process("path1"), t);
    }

    @Test(expected = FileNotFoundException.class)
    public void testSolution2() throws IOException {
        var t = new HashSet<String>();
        t.add("test");
        Assert.assertEquals(sol.process("incorrect_path"), t);
    }
    @Test
    public void testCalls() throws IOException {
        sol.process("path1");
        verify(s, times(1)).getData("path1");
    }
}