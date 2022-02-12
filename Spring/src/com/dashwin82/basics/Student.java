package com.dashwin82.basics;

public class Student {

    public String name;

    public void setName(String name)
    {
        this.name = name;
    }

    public String getName()
    {
        return name;
    }

    public void destroy() {
        System.out.println("Student(name: " + name + ") is destroyed");
    }
}
