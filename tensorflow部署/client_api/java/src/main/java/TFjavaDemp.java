import org.tensorflow.*;
import org.tensorflow.Graph;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

// tensorflow模型跨平台上线方案之跨语言API方式
// 添加jdk-1.8



public class TFjavaDemp {
    public static void main(String args[]){
        byte[] graphDef = loadTensorflowModel("rf.pb");
        // 生成测试数据
        float inputs[][] = new float[4][6];
        for(int i=0;i<4;i++){
            for(int j=0;j<6;j++){
                if(i<2){
                    inputs[i][j] = 2*i - 5*j-6;
                }else{
                    inputs[i][j] = 2*i+5*j-6;
                }
            }
        }
        Tensor<Float> input = covertArrayToTensor(inputs);  // 二维数组转换tensor
        Graph g = new Graph();
        g.importGraphDef(graphDef);    // 加载计算图
        Session s = new Session(g);
        Tensor result = s.runner().feed("input",input).fetch("output").run().get(0);

        long[] rshape = result.shape();
        int rs = (int) rshape[0];
        long realResult[] = new long[rs];
        result.copyTo(realResult);

        for(long a: realResult){
            System.out.println(a);
        }
    }

    static private byte[] loadTensorflowModel(String path){
        try{
            return Files.readAllBytes(Paths.get(path));
        } catch (IOException e){
            e.printStackTrace();
        }
        return null;
    }

    static private Tensor<Float> covertArrayToTensor(float inputs[][]){
        return Tensors.create(inputs);
    }
}
