function [w1 w2 iteration] = perceptron1(train_data,theta)
    w = [0;0;0;0;0];
    class_total = [];
    class_else = [];
    for i = 1:length(train_data(:,1))
        if(train_data(i,5) > 1)
            train_temp = [(-1)*train_data(i,1:4),-1];
            class_total = [class_total;train_temp];
            class_else = [class_else;train_data(i,:)];
        else
            class_total = [class_total;train_data(i,:)];
        end
    end
    [w1 iteration1] = perc(class_total,theta);
    class = [];
    for j = 1:length(class_else(:,1))
        if(class_else(j,5) > 2)
            train_temp = [(-1)*class_else(j,1:4),-1];
            class = [class;train_temp];
        else
            class = [class;class_else(j,:)];
        end
    end
    [w2 iteration2] = perc(class,theta);
    iteration = iteration1 + iteration2;
end
