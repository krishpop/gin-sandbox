import gin
import runner

def main():
    runner.run()

if __name__ == '__main__':
    gin.parse_config_file('test.gin')
    gin.finalize()
    main()
    with gin.unlock_config():
        gin.parse_config_file('test2.gin')
    main()

