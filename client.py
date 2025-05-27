import grpc
import asciiart_pb2
import asciiart_pb2_grpc

def run():
    server_id_addrs="192.168.0.103"
    # Replace 'server-ip-address' with actual server IP
    channel = grpc.insecure_channel(f"{server_id_addrs}:50051")
    stub = asciiart_pb2_grpc.AsciiArtServiceStub(channel)
    
    while True:
        print("\n1. Generate ASCII Art")
        print("2. List Available Styles")
        print("3. Exit")
        choice = input("Select option: ")
        
        if choice == '3':
            break
            
        if choice == '1':
            text = input("Enter text to convert: ")
            # Get available styles first
            styles = stub.GetArtStyles(asciiart_pb2.StyleRequest())
            print("\nAvailable styles:")
            for i, style in enumerate(styles.styles[:10]):  # Show first 10
                print(f"{i+1}. {style}")
            style_choice = int(input("Select style number: ")) - 1
            selected_style = styles.styles[style_choice]
            
            response = stub.GenerateArt(asciiart_pb2.ArtRequest(
                text=text, style=selected_style
            ))
            print("\nGenerated Art:")
            print(response.art)
            
        elif choice == '2':
            response = stub.GetArtStyles(asciiart_pb2.StyleRequest())
            print("\nAvailable Styles:")
            for style in response.styles[:20]:  # Show first 20
                print(style)

if __name__ == '__main__':
    run()
