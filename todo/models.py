from django.db import models
import os

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    upload = models.ImageField(upload_to='uploads/')  # The upload path can be anything

    def save(self, *args, **kwargs):
        # If there's already a file, delete the old one to prevent duplication
        if self.pk:
            existing_instance = MyModel.objects.get(pk=self.pk)
            if existing_instance.upload != self.upload:
                existing_instance.upload.delete(save=False)

        # Generate the new filename
        count = MyModel.objects.count() + 1
        extension = os.path.splitext(self.upload.name)[1]  # Get file extension
        new_filename = f'meme{count}{extension}'

        # Set the new filename
        self.upload.name = new_filename

        # Call the original save method
        super(MyModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
