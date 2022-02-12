package com.dashwin82.basics;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.util.List;

public class TestRefApplicationContext {

    public static void main(String[] args){

        ApplicationContext context = new ClassPathXmlApplicationContext(
                "applicationContextExample2.xml");

        Teacher ref = context.getBean("teacher", Teacher.class);
        //ref.addCourse(); //postconstruct annotation does not work, as it was not a container managed bens
        List<Course> courses = ref.getCourses();

        System.out.println(courses);

    }
}
