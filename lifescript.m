clear;
keystrokes=zeros(1000000,1);
keystrokes=char(keystrokes);
filename = 'null';
sumVec=zeros(9,1);
for j=1:2000
    j
    len=498; GRID=int8(rand(len,len));
    up=[2:len 1]; down=[len 1:len-1]; %the world is round
    colormap(gray(2));
    for i=1:500
        k = ((500*(j-1))+i);
        clear(filename);
        kStr = num2str(k);
        filename = strcat('./life_frames/',kStr,'.png');
        neighbours=GRID(up,:)+GRID(down,:)+GRID(:,up)+GRID(:,down)+...
        GRID(up,up)+GRID(up,down)+GRID(down,up)+GRID(down,down);
        GRID = neighbours==3 | GRID & neighbours==2;
        imwrite(GRID,filename);
        sumVec(1,1) = sum(sum(GRID(1:166,1:166)));
        sumVec(2,1) = sum(sum(GRID(167:332,1:166)));
        sumVec(3,1) = sum(sum(GRID(333:498,1:166)));
        sumVec(4,1) = sum(sum(GRID(1:166,167:332)));
        sumVec(5,1) = sum(sum(GRID(167:332,167:332)));
        sumVec(6,1) = sum(sum(GRID(333:498,167:332)));
        sumVec(7,1) = sum(sum(GRID(1:166,333:498)));
        sumVec(8,1) = sum(sum(GRID(167:332,333:498)));
        sumVec(9,1) = sum(sum(GRID(333:498,333:498)));
        if (sumVec(1,1)==max(sumVec))
            keystrokes(k,1)='A';
        elseif (sumVec(2,1)==max(sumVec))
            keystrokes(k,1)='U';
        elseif (sumVec(3,1)==max(sumVec))
            keystrokes(k,1)='B';
        elseif (sumVec(4,1)==max(sumVec))
            keystrokes(k,1)='L';
        elseif (sumVec(5,1)==max(sumVec))
            keystrokes(k,1)= keystrokes((k-1),1);
        elseif (sumVec(6,1)==max(sumVec))
            keystrokes(k,1)='R';
        elseif (sumVec(7,1)==max(sumVec))
            keystrokes(k,1)='T';
        elseif (sumVec(8,1)==max(sumVec))
            keystrokes(k,1)='D';
        elseif (sumVec(9,1)==max(sumVec))
            keystrokes(k,1)='E';
        end
    end
end
save('keys.mat','keystrokes');
dlmwrite('raw_keys.txt',keystrokes);
    
        
        