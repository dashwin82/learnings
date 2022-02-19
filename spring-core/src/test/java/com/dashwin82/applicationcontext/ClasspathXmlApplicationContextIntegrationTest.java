package com.dashwin82.applicationcontext;


import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.context.MessageSource;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.util.List;
import java.util.Locale;

import static org.hamcrest.core.IsEqual.equalTo;
import static org.junit.Assert.assertThat;

public class ClasspathXmlApplicationContextIntegrationTest {
    @Test
    public void testApplicationContextAware() {
        ApplicationContext context = new ClassPathXmlApplicationContext("classpathxmlapplicationcontext-example.xml");
        Teacher teacher = context.getBean("teacher", Teacher.class);
        List<Course> courses = teacher.getCourses();
        assertThat(courses.size(), equalTo(1));
        assertThat(courses.get(0).getName(), equalTo("math"));
    }
}