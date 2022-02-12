package com.dashwin82.basics;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import javax.annotation.PostConstruct;
import java.util.ArrayList;
import java.util.List;

//public class Teacher implements ApplicationContextAware {
public class Teacher {

    @Autowired
    private ApplicationContext context;
    private List<Course> courses = new ArrayList<Course>();

/*    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        System.out.println("setApplicationContext");
        this.context = applicationContext;
    }

 */

    public Teacher() {
    }

    @PostConstruct
    public void addCourse(){
        System.out.println("Post construct : addCourse");
        if(context.containsBean("math")) {
            courses.add(context.getBean("math", Course.class));
        }
        if(context.containsBean("physics")) {
            courses.add(context.getBean("math", Course.class));
        }
    }

    public  List<Course> getCourses() {
        return courses;
    }

    public void setCourses(List<Course> courses) {
        this.courses = courses;
    }
}
