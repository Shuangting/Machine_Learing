function right_rate = testperc(transmatrix1,transmatrix2,test_data)
	count = 0;
    for i = 1:length(test_data(:,1))
        if([test_data(i,1:4),1]*transmatrix1 > 0) % Type1
            test_result(i) = 1;
        else
            if([test_data(i,1:4),2]*transmatrix2 > 0)   % Type2
                test_result(i) = 2;
            else
                test_result(i) = 3;
            end
        end
        if(test_data(i,5) - test_result(i) < 0.001)
            count = count + 1;
        else
            count = count;
        end
    end
    right_rate = count/length(test_data(:,1));
end

