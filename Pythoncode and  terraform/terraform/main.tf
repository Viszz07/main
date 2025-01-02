resource "null_resource" "file" {
    provisioner "local-exec" {
        command = "echo 'welcome ${upper("vishal")} to terraform' > output.txt "
    }
  
}
variable "example" {
  type = string
  description = "this is a tem descp"
  default = "value"
}