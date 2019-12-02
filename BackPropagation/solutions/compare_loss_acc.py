history = keras_model.history.history
fig = plt.figure(figsize=(20,5))
ax = fig.add_subplot(1,2,1)
ax.plot(history["loss"], label="keras", color="red")
ax.plot(history["val_loss"], label="keras_test", linestyle="dashed" ,color="red")
ax.plot(losses, label="numpy", color="blue")
ax.plot(losses_test, label="numpy_test", color="blue")
ax.set_xlabel("Epochs")
ax.set_ylabel("Loss")
ax.set_title("Training loss")
ax.legend(loc='best')
ax = fig.add_subplot(1,2,2)
ax.plot(history["acc"], label="keras", color="red")
ax.plot(history["val_acc"], label="keras_test", linestyle="dashed" ,color="red")
ax.plot(accuracies, label="numpy", color="blue")
ax.plot(accuracies, label="numpy_test", color="blue")
ax.set_ylabel("accuracy")
ax.set_xlabel("Epochs")
ax.legend(loc='best')
ax.set_title("Accuracy")