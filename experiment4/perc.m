function [w iteration] = perc(class_total,theta)
    w = [0;0;0;0;0];
    % find the optimal vector
    counter = 0;
    iteration = 0;
    flagexit = 0;
    m = length(class_total(:,1));
    while(flagexit == 0)
        for j = 1:m
            tempt_result = class_total(j,:) * w;
            if(tempt_result > 0)
                iteration = iteration + 1;
                w = w;
                counter = counter + 1;
            else
                iteration = iteration + 1;
                w = w + theta * (class_total(j,:))';
                counter = 0;
            end
        end
        if(counter >= m)
            flagexit = 1;
        else
            flagexit = 0;
        end
    end
end
