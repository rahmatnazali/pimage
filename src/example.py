from pimage import copy_move

fraud_list, ground_truth_image, result_image = copy_move.detect("../assets/dataset_example_blur.png",
                                                                block_size=32,
                                                                verbose=True)

print(fraud_list)
print(ground_truth_image.size)
print(result_image.size)