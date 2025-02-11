#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    try {
      const tasks = JSON.parse(body);
      const completedTasks = {};

      tasks.forEach(task => {
        if (task.completed) {
          if (completedTasks[task.userId]) {
            completedTasks[task.userId]++;
          } else {
            completedTasks[task.userId] = 1;
          }
        }
      });

      console.log(completedTasks);
    } catch (parseError) {
      console.log('Error parsing JSON:', parseError);
    }
  }
});
