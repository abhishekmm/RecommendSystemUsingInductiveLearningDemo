<<<<<<< HEAD
import tensorflow as tf, sys

image_path = sys.argv[1]
#image_path='D:\\RecommendSystemUsingInductiveLearningDemo\\upload\\temp\\download.jpg'
# Read in the image_data
#image_data = tf.gfile.FastGFile('/home/tensorflow/tensorflow/examples/method3mod/dataset/dataset/T', 'rb').read()
image_data = tf.gfile.FastGFile(image_path, 'rb').read()


# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
                   # in tf.gfile.GFile("/tf_files/retrained_labels.txt")]
                   in tf.gfile.GFile("retrained_labels1.txt")]

# Unpersists graph from file
# with tf.gfile.FastGFile("/tf_files/retrained_graph.pb", 'rb') as f:
with tf.gfile.FastGFile("D:/RecommendSystemUsingInductiveLearningDemo/transferlearnmodels/retrained_graph_specs.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
    predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg/contents:0': image_data})
    
    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score))
=======
import tensorflow as tf, sys

image_path = sys.argv[1]
#image_path='D:\\RecommendSystemUsingInductiveLearningDemo\\upload\\temp\\download.jpg'
# Read in the image_data
#image_data = tf.gfile.FastGFile('/home/tensorflow/tensorflow/examples/method3mod/dataset/dataset/T', 'rb').read()
image_data = tf.gfile.FastGFile(image_path, 'rb').read()


# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
                   # in tf.gfile.GFile("/tf_files/retrained_labels.txt")]
                   in tf.gfile.GFile("retrained_labels1.txt")]

# Unpersists graph from file
# with tf.gfile.FastGFile("/tf_files/retrained_graph.pb", 'rb') as f:
with tf.gfile.FastGFile("D:/RecommendSystemUsingInductiveLearningDemo/transferlearnmodels/retrained_graph_specs.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
    predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg/contents:0': image_data})
    
    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score))
>>>>>>> ba84b7d6234a962fe8d0186a07338684f1d6e918
