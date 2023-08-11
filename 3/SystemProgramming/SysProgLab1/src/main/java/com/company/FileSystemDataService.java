package com.company;

import java.io.FileNotFoundException;
import java.io.IOException;

public interface FileSystemDataService{
    public String getData(String path) throws IOException, FileNotFoundException;
}
